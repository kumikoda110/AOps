#!/usr/bin/python
#-*- coding: utf-8 -*-


import hashlib
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import db
import conf


class User(object):
    # 初始化类
    def __init__(self, phone=None, passwd=None, reg_info=None):
        self.conn, self.cur = db.db_object()
        self.phone = phone
        self.passwd = passwd
        self.reg_info = reg_info

    # 查看用户是否存在
    def user_exist(self):
        query = 'SELECT phone FROM user WHERE phone={phone}'.format(phone=self.phone)
        if self.cur.execute(query):
            return True  # 用户存在
        else:
            return False  # 用户不存在

    # 查看用户状态
    def user_status(self):
        query = 'SELECT status FROM user WHERE phone={phone}'.format(phone=self.phone)
        self.cur.execute(query)
        status = self.cur.fetchone()[0]
        if status == 1:
            return True  # 用户激活
        else:
            return False  # 用户未激活

    # 验证密码
    def check_pass(self):
        query = 'SELECT passwd FROM user WHERE phone={phone}'.format(phone=self.phone)
        self.cur.execute(query)
        dpasswd = self.cur.fetchone()[0]  # 数据库取的密码
        self.cur.close();
        self.conn.close()  # 关闭数据库
        self.passwd = hashlib.md5(self.passwd).hexdigest()
        if self.passwd == dpasswd:
            return True
        else:
            return False

    # 登陆
    def login(self):
        if not self.user_exist():
            result = {
                'code': 1,
                'message': conf._code.get(1, '用户不存在')
            }
            return result
        elif not self.user_status():
            result = {
                'code': 2,
                'message': conf._code.get(2, '用户未激活')
            }
            return result
        elif not self.check_pass():
            result = {
                'code': 3,
                'message': conf._code.get(3, '密码输入错误')
            }
            return result
        else:
            result = {
                'code': 0,
                'message': conf._code.get(0, '成功')
            }
            return result

    # 判断信息完整度
    def check_reg_info(self):
        # 判断子集
        y = self.reg_info.keys()
        if 'phone' in y and 'passwd' in y and 'class_type' in y and 'class_num' in y and 'en_passwd' in y:
            return True
        else:
            return False

    # 判断用户手机号正确性
    def check_phone(self):
        par = r'^1[3|4|5|7|8]\d{9}$'
        if re.match(par, self.phone):
            return True
        else:
            return False

    # 判断用户提交的密码是否一致
    def check_enpasswd(self):
        if self.reg_info['passwd'] == self.reg_info['en_passwd']:
            return True
        else:
            return False

    # 注册
    def reg(self):
        self.phone = self.reg_info['phone']
        if self.user_exist():  # 如果存在，不允许注册
            result = {
                'code': 55,
                'message': conf._code.get(55, '手机号已存在，请更换手机号')
            }
            return result

        if not self.check_reg_info():  # 填写完整度
            result = {
                'code': 51,
                'message': conf._code.get(51, '请填写相应信息')
            }
            return result
        elif not self.check_phone():  # 手机号是否正确
            result = {
                'code': 52,
                'message': conf._code.get(52, '用户手机号不正确')
            }
            return result
        elif not self.check_enpasswd():
            result = {
                'code': 53,
                'message': conf._code.get(53, '密码不一致')
            }
            return result
        else:
            passwd = hashlib.md5(self.reg_info['passwd']).hexdigest()
            query = '''
                    INSERT INTO user (
                        phone,
                        passwd,
                        class_type,
                        class_num
                    )
                    VALUE
                        (
                            '{phone}',
                            '{passwd}',
                            '{class_type}',
                            '{class_num}'
                        )
                '''.format(phone=self.reg_info['phone'],
                           passwd=passwd,
                           class_type=self.reg_info['class_type'],
                           class_num=self.reg_info['class_num'])
            try:
                self.cur.execute(query)
                self.conn.commit()
                self.cur.close();
                self.conn.close()
                result = {
                    'code': 0,
                    'message': '注册成功'
                }
                return result
            except Exception, e:
                result = {
                    'code': 54,
                    'message': str(e)
                }
                return result

    # 查看用户信息
    def user_info(self):
        query = 'SELECT id,phone,passwd,class_type,class_num,sex,qq,status FROM user'
        try:
            self.cur.execute(query)
            data = self.cur.fetchall()
            self.cur.close();
            self.conn.close()
            result = {
                'code': 0,
                'message': conf._code.get(0, '成功'),
                'result': {
                    'data': data
                }
            }
            return result
        except Exception, e:
            result = {
                'code': 56,
                'message': str(e)
            }

    def status_on(self):
        query = 'UPDATE user SET status=1 WHERE phone={phone}'.format(phone=self.phone)
        try:
            if not self.check_phone():
                result = {
                    'code': 52,
                    'message': conf._code.get(52, '用户手机号不正确')
                }
                return result
            elif not self.user_exist():
                result = {
                    'code': 1,
                    'message': conf._code.get(1, '用户不存在')
                }
                return result
            else:
                print query
                self.cur.execute(query)
                self.conn.commit()
                self.cur.close();
                self.conn.close()
                result = {
                    'code': 0,
                    'message': conf._code.get(0, '成功')
                }
                return result
        except Exception, e:
            result = {
                'code': 57,
                'message': str(e)
            }
            return result


if __name__ == '__main__':
    # 用户登陆测试
    u = User(phone=15010220814, passwd='jf123456')
    result = u.login()
    print result
    print result['message']

    # 用户注册测试
    reg_info = {
        'phone': '15010220816',
        'passwd': 'jf123456',
        'class_type': 'python',
        'class_num': '3',
        'en_passwd': 'jf123456'
    }
    u = User(reg_info=reg_info)
    result = u.reg()
    print result
    print result['message']

    # 用户查看所有信息测试
    u = User()
    print u.user_info()

    # 用户激活测试
    u = User(phone='15010220816')
    result = u.status_on()
    print result
    print result['message']

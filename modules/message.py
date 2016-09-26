#!/usr/bin/python
#-*- coding: utf-8 -*-


# coding:utf8

# set windows charset
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import conf
import requests
import db


class Message(object):
    """docstring for Message"""

    def __init__(self, url=conf.message_info['url'],
                 user=conf.message_info['user'],
                 passwd=conf.message_info['passwd']):
        self.url = url
        self.user = user
        self.passwd = passwd
        self.smsbao_code = {
            30: '密码错误',
            40: '账号不存在',
            41: '余额不足',
            42: '帐号过期',
            43: 'IP地址限制',
            50: '内容含有敏感词',
            51: '手机号码不正确',
            -1: '参数不全'
        }
        # 数据库对象
        self.conn, self.cur = db.db_object()

    # 获取短信日志
    def log(self):
        try:
            query = 'SELECT id,phone,content,status FROM message_log'
            self.cur.execute(query)
            data = self.cur.fetchall()
            result = {
                'code': 0,
                'message': '获取短信成功',
                'data': data
            }
            return result
        except Exception, e:
            result = {
                'code': 107,
                'message': '获取短信日志失败:' + str(e)
            }
            return result

    # 短信使用情况
    def usage(self):
        # 0 0,2702
        try:
            url = 'http://www.smsbao.com/query'
            payload = {
                'u': self.user,
                'p': self.passwd
            }
            r = requests.get(url, params=payload)
            ret = r.text
            if ret.isdigit():
                code = int(ret)
                result = {
                    'code': 106,
                    'message': self.smsbao_code[code]
                }
            else:
                code, data = ret.split()
                data = data.split(',')
                data = [int(data[0]), int(data[1])]

                result = {
                    'code': 0,
                    'message': '获取短信余额成功',
                    'result': {
                        'data': data
                    }
                }
            return result

        except Exception, e:
            result = {
                'code': 106,
                'message': str(e)
            }

    # 发送短信
    def send(self, phone, content):
        payload = {
            'u': self.user,
            'p': self.passwd,
            'm': phone,
            'c': content
        }
        try:
            r = requests.get(self.url, params=payload)
            sms_code = r.text

            if sms_code.isdigit():  # 返回结果是否可转数字
                code = int(sms_code)
                if not code:  # 发送成功
                    result = {
                        'code': 0,
                        'message': '短信发送成功',
                        'data': {
                            'phone': phone,
                            'content': content
                        }
                    }
                else:  # 返回短信发送错误信息
                    result = {
                        'code': 102,
                        'message': self.smsbao_code[code]

                    }

            # -1单独处理
            elif sms_code == '-1':
                result = {
                    'code': 102,
                    'message': '参数不全'
                }
            else:
                result = {
                    'code': 102,
                    'message': '短信发送失败'
                }
            # 写日志
            if not result['code']:
                status = 1
            else:
                status = 0
            query = '''
                INSERT INTO message_log (phone, content, status)
                VALUES
                    ('{phone}', '{content}', {status})
            '''.format(phone=phone, content=content, status=status)
            try:
                self.cur.execute(query)
                self.conn.commit()
                result['log'] = True
            except Exception, e:
                result['log'] = False
            result['phone'] = phone
            result['content'] = content
            return result

        except Exception, e:
            result = {
                'code': 101,
                'message': str(e)
            }
            return result

    # 上课通知
    def notify(self, class_type='python',
               class_num=3,
               ntime='晚上8点',
               class_content='到了你就知道'):
        result = {
            'code': 0,
            'message': 'success',
            'data': {}
        }

        query = '''
            SELECT
                phone,
                username
            FROM
                user
            WHERE
                class_type = '{class_type}'
            AND class_num = {class_num}
            AND status = 1;
            '''.format(class_type=class_type,
                       class_num=class_num)
        try:
            if self.cur.execute(query):
                phones = self.cur.fetchall()  # (().())
                for phone, username in phones:
                    content = '【京峰课堂】尊敬的{username}:我们将于{ntime}进行{class_type}上课，上课内容为[{class_content}],请准时上课。'
                    t_content = content.format(username=username,
                                               ntime=ntime,
                                               class_type=class_type,
                                               class_content=class_content)
                    # 过手机号批量发送短信，并获得发送此短信的结果
                    p_ret = self.send(phone=phone, content=t_content)
                    result['data'][phone] = p_ret
                return result

            else:
                result = {
                    'code': 103,
                    'message': '发送上课通知时查不到用户，请修改你的条件'
                }
                return result
        except Exception, e:
            result = {
                'code': 104,
                'message': str(e)
            }
            return result


if __name__ == '__main__':
    m = Message()
    print m.send(150102208148, '测试一下短信接口')
    # m.notify(class_num=1)

    # print result
    # print m.log()

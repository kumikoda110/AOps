#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')

db_info = {
        "host" : "192.168.0.10",
        "port" : 3306,
        "user" : "root",
        "passwd" : "p@ssw0rd",
        "db" : "aops",
        "charset" : "utf8"
    }

#message api info
message_info = {
            'url' : 'http://api.smsbao.com/sms',
            'user' : 'kumikoda',
            'passwd' : '1b2853a309fb00d6934ff7bcfce8d281'
}

'''
0 正确
1-100 用户类错误
    1-50 登陆
    50-100 注册
    101-200 短信宝的错误
'''

_code = {
	0 : '成功' ,
	1 : '用户不存在' ,
	2 : '用户未激活' ,
	3 : '密码输入错误' ,
    4 : '请填写正确完整信息',
    51 : '请填写相应信息',
    52 : '用户手机号不正确',
    53 : '密码不一致' ,
    54 : '注册失败' ,
    55 : '手机号已存在，请更换手机号',
    56 : '查询所有用户时出错' ,
    57 : '用户激活失败',
    58 : '密码小于8个字符',
    59 : '修改用户失败',
    60 : '查询用户失败',
    101 : '短信接口错误，请联系管理员处理。',
    102 : '短信发送失败',
    103 : '发送上课通知时查不到用户，请修改你的条件',
    104 : '短信接口连接数据库失败',
    105 : '发送短信时写入日志时出错',
    106 : '获取短信余额错误',
    107 : '获取短信日志失败',
    201 : '无此方法',
    202 : '数据库执行失败',
    203 : '服务器不支持get/post以外的请求',
    204 : '请提交正确的URL',
}

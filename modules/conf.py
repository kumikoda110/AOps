#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')

db_info = {
        "host" : "211.166.22.190",
        "port" : 3306,
        "user" : "aops",
        "passwd" : "aops_pass",
        "db" : "aops",
        "charset" : "utf8"
    }

'''
0 正确
1-100 用户类错误
    1-50 登陆
    50-100 注册
'''
_code = {
	0 : '成功' ,
	1 : '用户不存在' ,
	2 : '用户未激活' ,
	3 : '密码输入错误' ,
    51 : '请填写相应信息',
    52 : '用户手机号不正确',
    53 : '密码不一致' ,
    54 : '注册失败' ,
    55 : '手机号已存在，请更换手机号',
    56 : '查询所有用户时出错' ,
    57 : '用户激活失败'
}

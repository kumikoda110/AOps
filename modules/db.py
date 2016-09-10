#!/usr/bin/python
#-*- coding: utf-8 -*-


import MySQLdb
import conf

#数据库连接
def db_object():
    db_info = conf.db_info
    try:
        conn = MySQLdb.connect(**db_info)
        cur = conn.cursor()
        return conn,cur
    except Exception, e:
        raise e
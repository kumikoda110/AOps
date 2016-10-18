#!/usr/bin/python
#-*- coding: utf-8 -*-


# set windows charset
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import db, conf


class Cmdb(object):
    """docstring for Cmdb"""

    def __init__(self):
        self.conn, self.cur = db.db_object()

    # 机房方法
    # 添加机房
    def add_room(self, info):
        query = 'INSERT INTO room(info) VALUES("{info}")'.format(info=info)
        try:
            self.cur.execute(query)
            self.conn.commit()
            return {'code': 0, 'message': '添加机房  {0}  成功'.format(info)}
        except Exception, e:
            return {'code': 202, 'message': '数据库执行失败' + str(e)}

    # 修改机房
    def edit_room(self, id, info):
        query = 'UPDATE room set info="{info}" WHERE id="{id}"'.format(id=id,
                                                                       info=info)
        try:
            self.cur.execute(query)
            self.conn.commit()
            return {'code': 0, 'message': '修改机房  {0}  成功'.format(info)}
        except Exception, e:
            return {'code': 202, 'message': '数据库执行失败' + str(e)}

    # 删除机房
    def del_room(self, id):
        query = 'DELETE fROM room WHERE id="{id}"'.format(id=id)
        try:
            self.cur.execute(query)
            self.conn.commit()
            return {'code': 0, 'message': '删除机房成功'}
        except Exception, e:
            return {'code': 202, 'message': '数据库执行失败' + str(e)}

    # 机房列表
    def list_room(self):
        query = 'SELECT id,info FROM room'
        try:
            self.cur.execute(query)
            data = self.cur.fetchall()
            return {'code': 0, 'message': '获取机房列表成功', 'data': data}
        except Exception, e:
            return {'code': 202, 'message': '数据库执行失败' + str(e)}

    # 机柜方法
    # 添加机柜
    def add_cabinet(self, info):
        query = 'INSERT INTO cabinet(info) VALUES("{info}")'.format(info=info)
        self.cur.execute(query)
        self.conn.commit()
        return {'code': 0, 'message': '添加机柜  {0}  成功'.format(info)}

    # 删除机柜
    def del_cabinet(self, id):
        query = 'DELETE fROM cabinet WHERE id="{id}"'.format(id=id)
        self.cur.execute(query)
        self.conn.commit()
        return {'code': 0, 'message': '删除机柜成功'}

    # 机柜列表
    def list_cabinet(self):
        query = 'SELECT id,info FROM cabinet'
        self.cur.execute(query)
        data = self.cur.fetchall()
        return {'code': 0, 'message': '获取机柜列表成功', 'data': data}

    # 修改机柜
    def edit_cabinet(self, id, info):
        query = 'UPDATE cabinet set info="{info}" WHERE id="{id}"'.format(id=id,
                                                                          info=info)
        self.cur.execute(query)
        self.conn.commit()
        return {'code': 0, 'message': '修改机柜成功'}

    # 主机方法
    # 添加主机
    def add_host(self, appliction, ip, port, username, password,
                 cpu, mem, disk, room_id, cabinet_id, location):
        query = '''
			INSERT INTO cmdb(
				appliction,
				ip,
				port,
				username,
				password,
				cpu,
				mem,
				disk,
				room_id,
				cabinet_id,
				location
			)
			VALUES
				(
					'{appliction}',
					'{ip}',
					'{port}',
					'{username}',
					'{password}',
					{cpu},
					{mem},
					{disk},
					{room_id},
					{cabinet_id},
					{location}
				)
		'''.format(appliction=appliction, ip=ip, port=port,
                   username=username, password=password, cpu=cpu,
                   mem=mem, disk=disk, room_id=room_id,
                   cabinet_id=cabinet_id, location=location)
        self.cur.execute(query)
        self.conn.commit()
        return {'code': 0, 'message': '添加机器成功'}

    # 修改主机
    def edit_host(self, id, appliction, ip, port, username, password,
                  cpu, mem, disk, room_id, cabinet_id, location):
        query = '''
			UPDATE
				cmdb
			SET
				appliction='{appliction}',
				ip='{ip}',
				port='{port}',
				username='{username}',
				password='{password}',
				cpu='{cpu}',
				mem='{mem}',
				disk='{disk}',
				room_id='{room_id}',
				cabinet_id='{cabinet_id}',
				location='{location}'
			WHERE
				id={id}
		'''.format(id=id, appliction=appliction, ip=ip, port=port,
                   username=username, password=password, cpu=cpu,
                   mem=mem, disk=disk, room_id=room_id,
                   cabinet_id=cabinet_id, location=location)
        self.cur.execute(query)
        self.conn.commit()
        return {'code': 0, 'message': '修改机器成功'}

    # 删除主机
    def del_host(self, id):
        query = 'DELETE FROM cmdb WHERE id="{id}"'.format(id=id)
        self.cur.execute(query)
        self.conn.commit()
        return {'code': 0, 'message': '删除机器成功'}

    # 修改主机
    def list_host(self):
        query = '''
			SELECT
				cmdb.id,
				appliction,
				ip,
				cpu,
				mem,
				disk,
				room.info AS room_info,
				cabinet.info AS cabinet_info,
				location
			FROM
				cmdb,
				room,
				cabinet
			WHERE
				cmdb.room_id = room.id AND
			  cmdb.cabinet_id = cabinet.id
		'''
        self.cur.execute(query)
        data = self.cur.fetchall()
        return {'code': 0, 'message': '获取机器列表成功', 'data': data}


if __name__ == '__main__':
    c = Cmdb()
    # print c.del_host(10)
    # print c.edit_host(9,'web2','192.168.100.58',22,'root','zuoloveyou',4,4,300,1,13,1)
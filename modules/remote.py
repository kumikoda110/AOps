#!/usr/bin/python
#-*- coding: utf-8 -*-



import sys
reload(sys)
sys.setdefaultencoding('utf8')

import db,conf

import paramiko
class Remote():
    def __init__(self):
        self.conn, self.cur = db.db_object()

    def get_hosts(self):
        query = 'SELECT ip FROM cmdb'
        self.cur.execute(query)
        hosts = self.cur.fetchall()
        data = [ host[0] for host in hosts ]
        result = {
            'code' : 0,
            'message' : '获取主机列表成功',
            'data' : data
        }
        return result

    def run(self,ip, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            query = '''
                        SELECT
                            username,password,port
                        FROM
                            cmdb
                        WHERE
                            ip = "{ip}"
                    '''.format(ip=ip)
            self.cur.execute(query)
            user,passwd,port = self.cur.fetchone()
            ssh.connect(hostname=ip,username=user,password=passwd,port=port)
            stdin, stdout, stderr = ssh.exec_command(command)
            if stderr.read():
                result = {
                    'code' : 1 ,
                    'message' : 'remote command run error',
                    'data' : {
                        'content':stderr.read()
                    }
                }
            else:
                result = {
                    'code' : 0 ,
                    'message' : 'remote command run success',
                    'data' : {
                        'content':stdout.read()
                    }
                }
            result['ip'] =ip
            return result
        except Exception, e:
            result = {
                    'code' : 2 ,
                    'message' : str(e),
                }
            result['ip'] =ip
            return result

    def runs(self,info, command):
        result = {}
        for hostname in info:
            host_ret = self.run(host_info=info[hostname],command=command)
            result[hostname] = host_ret
        return result


    def get(self,host_info,rpath,lpath):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(**host_info)
            sftp = ssh.open_sftp()
            try:
                sftp.get(rpath,lpath)
                result = {
                    'code' : 0,
                    'message' : 'success'
                }
                return result
            except Exception, e:
                result = {
                    'code' :3 ,
                    'message' : str(e)
                }
        except Exception, e:
            result = {
                    'code' : 2 ,
                    'message' : str(e),
                }
            return result

    def gets(self, info, rpath, lpath):
        result = {}
        for hostname in info:
            _lpath = '{hostname}_{lpath}'.format(hostname=hostname,lpath=lpath)
            host_ret = self.get(host_info=info[hostname],
                                rpath=rpath,
                                lpath=_lpath)
            del _lpath
            result[hostname] = host_ret
        return result
if __name__ == '__main__':
    r = Remote()
    print r.run('192.168.0.12','uptime')


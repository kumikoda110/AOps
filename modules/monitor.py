#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')

import psutil

class Monitor(object):

    #cpu info
    def get_cpu_info(self):
        '''
        with open('/proc/loadavg') as fd:
            loads = fd.read().split(' ')[0]
        '''

        result = {
            'cpu_count' : psutil.cpu_count(logical=False),
            'cpu_logical_count' : psutil.cpu_count(),
            'cpu_percent' : psutil.cpu_percent(interval=3),
            #'loads':laods,
            'cpu_idle_time_percent':psutil.cpu_times_percent().idle
        }
        return result

    #mem info
    def get_mem_info(self):
        vm = psutil.virtual_memory()
        swap = psutil.swap_memory()
        swap_percent = int((1 - swap.free / float(swap.total)) * 100)
        vm_percent = int((1 - vm.free / float(vm.total)) * 100)
        result = {
            'swap':{
                'swap_total' : swap.total/1024/1024/1024,
                'swap_free' : swap.free/1024/1024/1024,
                'swap_percent' : swap_percent
            },
            'virtual_memory':{
                'vm_total': vm.total/1024/1024/1024,
                'vm_free': vm.free/1024/1024/1024,
                'vm_percent' : vm_percent
            }
        }
        return result

    #disk info
    def get_disk_info(self):
        pass

    #procs info
    def get_procs_info(self):
        pass

    #network info
    def get_network_info(self):
        pass

    #all
    def get_all_info(self):
        result = {}
        mems = self.get_mem_info()
        cpus = self.get_cpu_info()
        result['mems'] = mems
        result['cpus'] = cpus
        return result

if __name__ == '__main__':
    m = Monitor()
    print m.get_all_info()
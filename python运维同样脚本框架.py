'''
######################
NO.1  日常运维： opsmod.py
######################
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
__author__ = 'Zline'
 
import os
import sys
import time
import zipfile
import datetime
import getpass
import logging 
import subprocess
from subprocess import Popen
 
 
#src update package path
src_path = '/home/update'
 
#des update package path
des_path = {'app1': '/home/tomcat/app1',
        'app2': '/home/tomcat/app2',
        'app3': '/home/tomcat/app3'}
 
#src backup package path
bsrc_path_lt = {'tomcat': ['/tmp/2', '/tmp/1'],
           'apache': ['/usr/local/apache/conf'],
           'app': ['/tmp']}
 
#des backup package path
bdes_path = '/home/mrdTomcat/version_bak'
 
#service name and server start bin 
srv_up = {'app1': '/home/tomcat/bin/startup.sh',
       'apache': '/usr/local/apache/bin/apachectl start',
       'app2': '/home/app2/tomcat/bin/startup.sh'}
 
#service name and server stop bin 
srv_down = {'app1': '/home/tomcat/bin/shutdown.sh',
        'apache': '/usr/local/apache/bin/apachectl stop',
        'app2': '/home/app2/tomcat/bin/shutdown.sh'}
 
#server pidfile path
srv_pidfile = {'app1': '/var/run/app1/app.pid',
          'apache': '',
          'app2': ''}
 
 
#change return color
def G(s):
    return "%s[32;2m%s%s[0m"%(chr(27), s, chr(27))
def A(s):
    return "%s[36;2m%s%s[0m"%(chr(27), s, chr(27))
def R(s):
    return "%s[31;2m%s%s[0m"%(chr(27), s, chr(27))
 
 
def start(ServiceName):
    '''
        Desc: Start GameServer
 
        CLI Example:
                opsmod.py ServiceName start
    '''    
    pid = srv_pidfile[ServiceName]
    cmd = srv_up[ServiceName]
    logging.info('{0} start'.format(ServiceName))  
    if os.path.exists(pid):
        return R('GameServer is already running !')
    else:
        proc = Popen(cmd, shell=True)
        return G('Start GameServer is successful !')
 
 
def stop(ServiceName):
    '''
        Desc: Stop GameServer
 
        CLI Example:
                opsmod.py ServiceName stop
    '''    
    pid = srv_pidfile[ServiceName]
    cmd = srv_down[ServiceName]
    logging.info('{0} stop'.format(ServiceName))  
    if os.path.exists(pid):
        proc = Popen(cmd, shell=True)
        return G('Stop GameServer is running...,please wait !')
    else:
        return R('GameServer is already stopped !')
 
 
def status(ServiceName):
    '''
        Desc: Check GameServer Status
 
        CLI Example:
                opsmod.py ServiceName status
    '''    
    cmd = 'ps -ef|grep "{0}"|grep -v grep'.format(ServiceName)
    proc = Popen(cmd, stdout=subprocess.PIPE, shell=True)
    item = proc.stdout.read().split('\n')[:-2]
    its = '\n'.join(item)
    cot = len(item)
    ret = its + '\n' + '*'*80 + '\n' + 'The total of process is {0} !'.format(cot)
    logging.info('{0} status'.format(ServiceName))  
    return G(ret)
 
 
def update(ServiceName, Pkg):
    '''
        Desc: Update GameServer
 
        CLI Example:
                opsmod.py ServiceName update Pkg
    '''    
    logging.info('{0} update {1}'.format(ServiceName, Pkg))  
    if Pkg:
        fl = os.path.join(src_path, Pkg)
        try:
            zfile = zipfile.ZipFile(fl,'r')
            for filename in zfile.namelist():
                zfile.extract(filename, des_path[ServiceName])
            return G('Update is successful !')
        except IOError:
            return R('The package is invalid !!!')
    else:
        return R('The package is invalid !!!')
 
 
def backup(ServiceName):
    '''
        Desc: Backup GameServer
 
        CLI Example:
                opsmod.py ServiceName backup
    '''    
    logging.info('{0} backup'.format(ServiceName))  
    bakname = ServiceName + '_' +  datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.zip'
    zipname = os.path.join(bdes_path, bakname)
    f = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for bsrc_path in bsrc_path_lt[ServiceName]:
        bac_path = os.path.dirname(bsrc_path)
        ls_path = bac_path + '/'
        zg_path = bsrc_path.split(ls_path)[1]
        os.chdir(bac_path)
        for dirpath, dirnames, filenames in os.walk(zg_path):
            for filename in filenames:
                f.write(os.path.join(dirpath, filename)) 
    f.close()
    return G('Backup is successful !')
 
 
if __name__== "__main__":
    if os.path.exists('./logs'):
        pass
    else:
        os.makedirs('./logs')
    log_ft = datetime.datetime.now().strftime('%Y-%m-%d-%H') 
    user_cmd = getpass.getuser()
    logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s {0} %(levelname)s: %(message)s'.format(user_cmd),  
                    datefmt='%Y-%m-%d %H:%M:%S',  
                    filename='./logs/control{0}.log'.format(log_ft),  
                    filemode='a')  
    opts = sys.argv
    try:
        if opts[1]=='-d' or opts[1]=='--help':
            print G('start :') + R('{0}'.format(start.__doc__))
            print G('stop :') + R('{0}'.format(stop.__doc__))
            print G('status :') + R('{0}'.format(status.__doc__))
            print G('update :') + R('{0}'.format(update.__doc__))
            print G('backup :') + R('{0}'.format(backup.__doc__))
        elif opts[2]=='start':
            print start(opts[1])
        elif opts[2]=='stop':
            print stop(opts[1])
        elif opts[2]=='status':
            print status(opts[1])
        elif opts[2]=='backup':
            print backup(opts[1])
        elif opts[2]=='update':
            print update(opts[1], opts[3])
        else:
            print R('Script Parameter Error !!!')
    except IndexError:
        print R('Script Parameter Error !!!')
        
'''
######################
NO.2  CMDB通用API： cmdb-api.py
######################
'''
#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
   
import urllib   
import urllib2   
import json   


def hostname(IP):   
    url = 'http://www.baidu.com/restful/getAssetByIpAddress'   
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
    values = {'ipAddress': IP}   
    headers = {'User-Agent': user_agent}   
    data = urllib.urlencode(values)   
    req = urllib2.Request(url, data, headers)   
    response = urllib2.urlopen(req)   
    res = response.read()   
    data = json.loads(res)   
    return data
    
'''
######################
NO.3  Web扫描：  scan_web_banner.py
######################
'''
#/usr/bin/env python
#-*-coding=utf-8-*-

# __author__  = 'Zline'

import requests
import re
from threading import Thread,Lock
import time
import sys
import chardet
import netaddr
import struct
import socket

lock = Lock()

def ip2int(addr):
        return struct.unpack("!I", socket.inet_aton(addr))[0]
def int2ip(addr):
        return socket.inet_ntoa(struct.pack("!I", addr))
def int_dec(pagehtml):

        charset = None
        if pagehtml != '':
                # print 'use charset dect'
                enc = chardet.detect(pagehtml)
                # print 'enc= ', enc
                if enc['encoding'] and enc['confidence'] > 0.9:
                        charset = enc['encoding']

                if charset == None:
                        charset_re = re.compile("((^|;)\s*charset\s*=)([^\"']*)", re.M)
                        charset=charset_re.search(pagehtml[:1000]) 
                        charset=charset and charset.group(3) or None

                # test charset
                try:
                        if charset:
                                unicode('test',charset,errors='replace')
                except Exception,e:
                        print 'Exception',e
                        charset = None
        # print 'charset=', charset
        return charset


def http_banner(url):
        ip=url
        try:
                url=requests.get(url,timeout=2)        

                body = url.content
                
                charset = None
                if body != '':
                        charset = int_dec(body)

                if charset == None or charset == 'ascii':
                        charset = 'ISO-8859-1'

                if charset and charset != 'ascii' and charset != 'unicode':
                        try:
                                body = unicode(body,charset,errors='replace')
                        except Exception, e:
                                body = ''
                Struts=url.status_code
                Server=url.headers['server'][0:13]
                if Struts==200 or Struts==403 or Struts==401:
                        title=re.findall(r"<title>(.*)<\/title>",body)
                        if len(title):
                                title = title[0].strip()
                        else:
                                title = ''
                        lock.acquire()
                        print ('%s\t%d\t%-10s\t%s'%(ip.lstrip('http://'),Struts,Server,title))
                        lock.release()
        except (requests.HTTPError,requests.RequestException,AttributeError,KeyError),e:
                pass



if __name__ == '__main__':
        if len(sys.argv) >= 2:
                ips = sys.argv[1]
        else:
                print 'usage: python http_banner.py 192.168.1./24 '
                print 'usage: python http_banner.py 192.168.1.1-192.168.1.254 '
                print 'usage: python http_banner.py 192.168.1./24 8080'
                print 'usage: python http_banner.py 192.168.1.1-192.168.1.254 8080'
                sys.exit()
        port = '80'
        if len(sys.argv) == 3:
                port = sys.argv[2]
                
        if '-' in ips:
                start, end = ips.split('-')
                startlong = ip2int(start)
                endlong = ip2int(end)
                ips = netaddr.IPRange(start,end)
                for ip in list(ips):
                        url='http://%s:%s'%(ip,port)
                        t = Thread(target=http_banner,args=(url,))
                        t.daemon=False
                        t.start()
        elif '/'        in ips:
                ips = netaddr.IPNetwork(ips)
                for ip in list(ips):
                        url='http://%s:%s'%(ip,port) 
                        t = Thread(target=http_banner,args=(url,))
                        t.daemon=False
                        t.start()
                        
'''
######################
NO.4  Python八大排序算法的实现： psf.py
######################
'''
1、插入排序  
def insert_sort(lists):  
    # 插入排序  
    count = len(lists)  
    for i in range(1, count):  
        key = lists[i]  
        j = i - 1  
        while j >= 0:  
            if lists[j] > key:  
                lists[j + 1] = lists[j]  
                lists[j] = key  
            j -= 1  
    return lists  
   
2、希尔排序  
def shell_sort(lists):  
    # 希尔排序  
    count = len(lists)  
    step = 2  
    group = count / step  
    while group > 0:  
        for i in range(0, group):  
            j = i + group  
            while j < count:  
                k = j - group  
                key = lists[j]  
                while k >= 0:  
                    if lists[k] > key:  
                        lists[k + group] = lists[k]  
                        lists[k] = key  
                    k -= group  
                j += group  
        group /= step  
    return lists  
   
3、冒泡排序  
def bubble_sort(lists):  
    # 冒泡排序  
    count = len(lists)  
    for i in range(0, count):  
        for j in range(i + 1, count):  
            if lists[i] > lists[j]:  
                lists[i], lists[j] = lists[j], lists[i]  
    return lists  
   
4、快速排序  
def quick_sort(lists, left, right):  
    # 快速排序  
    if left >= right:  
        return lists  
    key = lists[left]  
    low = left  
    high = right  
    while left < right:  
        while left < right and lists[right] >= key:  
            right -= 1  
        lists[left] = lists[right]  
        while left < right and lists[left] <= key:  
            left += 1  
        lists[right] = lists[left]  
    lists[right] = key  
    quick_sort(lists, low, left - 1)  
    quick_sort(lists, left + 1, high)  
    return lists  
   
5、直接选择排序  
def select_sort(lists):  
    # 选择排序  
    count = len(lists)  
    for i in range(0, count):  
        min = i  
        for j in range(i + 1, count):  
            if lists[min] > lists[j]:  
                min = j  
        lists[min], lists[i] = lists[i], lists[min]  
    return lists  
   
6、堆排序  
# 调整堆  
def adjust_heap(lists, i, size):  
    lchild = 2 * i + 1  
    rchild = 2 * i + 2  
    max = i  
    if i < size / 2:  
        if lchild < size and lists[lchild] > lists[max]:  
            max = lchild  
        if rchild < size and lists[rchild] > lists[max]:  
            max = rchild  
        if max != i:  
            lists[max], lists[i] = lists[i], lists[max]  
            adjust_heap(lists, max, size)  
# 创建堆  
def build_heap(lists, size):  
    for i in range(0, (size/2))[::-1]:  
        adjust_heap(lists, i, size)  
# 堆排序  
def heap_sort(lists):  
    size = len(lists)  
    build_heap(lists, size)  
    for i in range(0, size)[::-1]:  
        lists[0], lists[i] = lists[i], lists[0]  
        adjust_heap(lists, 0, i)  
   
7、归并排序  
def merge(left, right):  
    i, j = 0, 0  
    result = []  
    while i < len(left) and j < len(right):  
        if left[i] <= right[j]:  
            result.append(left[i])  
            i += 1  
        else:  
            result.append(right[j])  
            j += 1  
    result += left[i:]  
    result += right[j:]  
    return result  
def merge_sort(lists):  
    # 归并排序  
    if len(lists) <= 1:  
        return lists  
    num = len(lists) / 2  
    left = merge_sort(lists[:num])  
    right = merge_sort(lists[num:])  
    return merge(left, right)  
   
8、基数排序  
import math  
def radix_sort(lists, radix=10):  
    k = int(math.ceil(math.log(max(lists), radix)))  
    bucket = [[] for i in range(radix)]  
    for i in range(1, k+1):  
        for j in lists:  
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)  
        del lists[:]  
        for z in bucket:  
            lists += z  
            del z[:]  
    return lists
    
    
'''
######################
NO.5  远程执行命令、远程添加信任、远程自动分区挂盘： ssh_cmd.py
######################
'''
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import argparse
import datetime
import paramiko

reload(sys)
sys.setdefaultencoding("utf-8")

username = 'root'
password = '123456'

rsa = [
'ssh-rsa1',
'ssh-rsa2'
]


#change return color
def G(s):
    return "%s[32;2m%s%s[0m"%(chr(27), s, chr(27))
def R(s):
    return "%s[31;2m%s%s[0m"%(chr(27), s, chr(27))
 

def cmd_exc(ip, username, password):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn.connect(hostname = ip, username = username, password = password, timeout = 5)
        stdin, stdout, stderr = conn.exec_command(cmd)
        result = stdout.readlines()
        ret = ''.join(result)
    except:
        print R("无法连接")
    conn.close()
    try:
        return G(ret)
    except UnboundLocalError:
        pass


def copy_rsa(ip, username, password):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn.connect(hostname = ip, username = username, password = password, timeout = 5)
        stdin, stdout, stderr = conn.exec_command("echo '{0}'>>/root/.ssh/authorized_keys;echo '{1}'>>/root/.ssh/authorized_keys".format(rsa[0], rsa[1]))
        result = stdout.readlines()
        ret = ''.join(result)
    except:
        print R("无法连接")
    conn.close()
    try:
        return G(ret)
    except UnboundLocalError:
        pass


def auto_disk(Disk):
    if os.path.exists('./auto_disk.sh'):
        os.remove('./auto_disk.sh') 
    with open('auto_disk.sh', 'a') as f:
        print >>f, '#!/bin/bash'
        print >>f, 'rpm -aq|grep expect'
        print >>f, 'if [ $? != 0 ];then'
        print >>f, '    yum install -y expect'
        print >>f, 'fi'
        print >>f, '/usr/bin/expect -c"'
        print >>f, 'set timeout -1'
        print >>f, 'spawn  /sbin/fdisk /dev/{0}'.format(Disk)
        print >>f, 'expect \"*m for help*:\"'
        print >>f, 'send -- \"n\r\"' 
        print >>f, 'expect \"*p*\n\"' 
        print >>f, 'send -- \"p\r\"'
        print >>f, 'expect  \"*number (1-4):\"' 
        print >>f, 'send -- \"1\r\"'
        print >>f, 'expect  \"*default 1*:\"'
        print >>f, 'send -- \"\r\"'
        print >>f, 'expect  \"*default*:\"' 
        print >>f, 'send -- \"\r\"'
        print >>f, 'expect  \"*m for help*:\"'
        print >>f, 'send -- \"w\r\"'
        print >>f, 'expect eof'
        print >>f, '"'
        print >>f, 'mkfs.ext4 /dev/{0}1'.format(Disk)
        print >>f, 'echo "/dev/{0}1    /home/    ext4   defaults  0  0" >> /etc/fstab'.format(Disk)
        print >>f, 'mount /dev/{0}1   /home/'.format(Disk)


def sftp_auto(ip, username, password):
    t = paramiko.Transport((ip,22))
    t.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put('./auto_disk.sh','/tmp/auto_disk.sh')
    t.close()
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn.connect(hostname = ip, username = username, password = password, timeout = 5)
        stdin, stdout, stderr = conn.exec_command('sh /tmp/auto_disk.sh')
        result = stdout.readlines()
        ret = ''.join(result)
    except:
        print R("无法连接")
    conn.close()
    try:
        return G(ret)
    except UnboundLocalError:
        pass
        


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='ssh_cmd', usage='%(prog)s [options]')
    parser.add_argument('-H','--host', nargs='?', dest='listhost', help='主机/多个主机用","分割')
    parser.add_argument('-f','--file', nargs='?', dest='filehost', help='主机列表文件')
    parser.add_argument('-m','--command', nargs='?', dest='command', help='执行命令')
    parser.add_argument('-I','--init', nargs='?', dest='init', help='自动分区挂盘')
    parser.add_argument('-A','--add', nargs='?', dest='add_rsa', help='添加信任')
    if len(sys.argv)==1:
        parser.print_help()
    else:
        args=parser.parse_args()
        cmd = args.command
        if args.listhost is not None and args.filehost is None: 
            if args.command is not None:
                for ip in args.listhost.split(','):
                    print G(ip) 
                    print G('-'*80)
                    print cmd_exc(ip, username, password)
                    print 
            elif args.init is not None:
                auto_disk(args.init)
                for ip in args.listhost.split(','):
                    print G(ip)
                    print G('-'*80)
                    print sftp_auto(ip, username, password)
                    print
            elif args.add_rsa == 'root':
                for ip in args.listhost.split(','):
                    print G(ip)
                    print G('-'*80)
                    print copy_rsa(ip, username, password)
                    print
            else:
                print R('功能选项为空')
        elif args.listhost is None and args.filehost is not None:
            if args.command is not None:
                try:
                    with open(args.filehost) as f:
                        for ips in f.readlines():
                            ip = ips.replace('\n', '')
                            print G(ip)
                            print G('-'*80)
                            print cmd_exc(ip, username, password)
                            print 
                except IOError:
                    print R('主机列表文件不存在')
            elif args.init is not None:
                auto_disk(args.init)
                for ip in args.listhost.split(','):
                    print G(ip)
                    print G('-'*80)
                    print sftp_auto(ip, username, password)
                    print
            elif args.add_rsa == 'root':
                for ip in args.listhost.split(','):
                    print G(ip)
                    print G('-'*80)
                    print copy_rsa(ip, username, password)
                    print
            else:
                print R('功能选项为空')
        else:
            print R('主机或命令不能为空')
            
            
'''
######################
NO.6  基于saltstack的nested输出的运维脚本： gameops.py
######################
'''
#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__ = 'Zline'

import os
import sys
import time
import zipfile
import datetime
import subprocess
import salt.client
from salt.output.nested import NestDisplay
from salt.utils import get_colors

#script path
sct_lt = {'start': '/home/game/startup.sh',
          'stop': '/home/game/shutdown.sh'
         }
#pid path
ser_pid = '/home/game/game.pid'
#src update package path
src_path = '/home/update'
#des update package path
des_path = '/home'
#src backup package path
bsrc_path_lt = ['/home/game/config', 
                '/home/game/data', 
                '/home/game/hibernate'] 
#des backup package path
bdes_path = '/home/backup'


# call salt output class
class NestPut(NestDisplay):
    def __init__(self):
        self.colors = get_colors(True)
        self.__dict__.update(get_colors(True))
        self.strip_colors = True

def Prest(data):
    '''
    Display ret data
    '''
    nest = NestPut()
    print '\n'.join(nest.display(data, 0, '', []))


def start():
    '''
    Define func start server
    '''
    if os.path.exists(ser_pid):
        return Prest('GameServer is already running !!!')
    else:
        cmd = sct_lt['start']
        proc = subprocess.Popen(cmd, shell=True)
        return Prest('Start GameServer is successful !!!')


def stop():
    '''
    Define func stop server
    '''
    if os.path.exists(ser_pid):
        cmd = sct_lt['stop']
        proc = subprocess.Popen(cmd, shell=True)
        return Prest('Stop GameServer is successful !!!')
    else:
        return Prest('GameServer is already stopped !!!')
      

def status():
    '''
    Define func status server
    '''
    if os.path.exists(ser_pid):
        return Prest('GameServer is not running !!!')
    else:
        cmd = 'ps -ef|grep \'{0}\'|grep -v grep'.format('server')
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        ret = proc.stdout.read() 
        return Prest(ret)


def backup():
    '''
    Define func backup server
    '''
    bakname = 'gs_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.zip'
    zipname = os.path.join(bdes_path, bakname)
    f = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for bsrc_path in bsrc_path_lt:
        bac_path = os.path.dirname(bsrc_path)
        ls_path = bac_path + '/'
        zg_path = bsrc_path.split(ls_path)[1]
        os.chdir(bac_path)
        for dirpath, dirnames, filenames in os.walk(zg_path):
            for filename in filenames:
                f.write(os.path.join(dirpath, filename)) 
    f.close()
    return 'Backup is successful !'


def update(pkg):
    '''
    Define func update server
    '''
    if pkg:
        fl = os.path.join(src_path, pkg)
        try:
            zfile = zipfile.ZipFile(fl,'r')
            for filename in zfile.namelist():
                zfile.extract(filename, des_path)
            return 'Update is successful !'
        except IOError:
            return 'The package is invalid !!!' 
    else:
        return 'The package is invalid !!!'



if __name__== "__main__":
    # check arguments
    opts = sys.argv
    if len(opts) < 2:
        print 'start|stop|status|backup|update'
        sys.exit(0)
    elif len(opts) == 2:
        if opts[1]=='start':
            start()
        elif opts[1]=='stop':
            stop()
        elif opts[1]=='status':
            status()
        elif opts[1]=='backup':
            backup()
        else:
            print 'Script Parameter Error !!!'
    elif len(opts) == 3:
        if opts[1]=='update':
            update(opts[2])
        else:
            print 'Script Parameter Error !!!'
    else:
        print 'Script Parameter Error !!!'
        
        
'''
######################
NO.7  日志监控脚本： monitor_log.py
######################
'''
#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import os
import time
import datetime
 
 
def GetLog(num):
    fls = []
    for dirpath, dirnames, filenames in os.walk('/opt/logbak'):
        for filename in filenames:
            fn = os.path.join(dirpath, filename)
            now_time = datetime.datetime.now()
            last_time = now_time + datetime.timedelta(days=-num)
            tg_time = last_time.strftime('%Y-%m-%d')
            endf = tg_time + '.tgz'
            if filename.startswith('xxx_') and filename.endswith(endf):
                if os.path.exists(fn):
                    fls.append(fn)
                else:
                    pass
            else:
                pass
     
    xlog = []
    for a in fls:
        xlog.append(a[13:17])
    xlog.sort()
    return xlog
 

blog = GetLog(2)
alog = GetLog(1)
'''
 交集:list(set(a).intersection(set(b))) 
 并集:list(set(a).union(set(b))) 
 差集:list(set(b).difference(set(a))) // b中有而a中没有的
'''
jdata = set(blog).intersection(set(alog)) #交集
mor = list(set(alog).difference(jdata))   #新增
les = list(set(blog).difference(jdata))   #减少
if len(mor) == 0 and len(les) == 0:
    print 0
elif len(mor) == 0 and len(les) != 0:
    print '-: {0}'.format(','.join(les))
elif len(mor) != 0 and len(les) == 0:
    print '+: {0}'.format(','.join(mor))
else:
    print '+: {jia}\n-: {shao}'.format(jia=','.join(mor), shao=','.join(les))


'''
######################
NO.8  生成Excel报表：  ssh_excel.py
######################
'''
#! /usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import xlwt
import time
import json
import urllib
import urllib2
import datetime
import paramiko
import commands


reload(sys)
sys.setdefaultencoding("utf-8")

username = 'root'
password = '123456'

url_idc = 'http://www.baidu.com/assetInfo' 
url_clound = 'http://www.tengxun.com/cloudAsset' 

def GetAllSeal(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
    if url == url_clound:
        values = {'test': 'demo'} 
    elif url == url_idc:
        values = {'product': u'运维'}
    else:
        return 'URL is Error !!!'
    headers = {'User-Agent': user_agent} 
    data = urllib.urlencode(values) 
    req = urllib2.Request(url, data, headers) 
    response = urllib2.urlopen(req) 
    res = response.read() 
    a = json.loads(res) 
    return a


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  

    font = xlwt.Font() 
    font.name = name 
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    return style

def WriteDateExcel():
    Tm = datetime.datetime.now().strftime('%Y-%m-%d')
    urls = [url_clound, url_idc]
    wbk = xlwt.Workbook(encoding='utf-8')
    for url in urls:
        result = GetAllSeal(url)
        if url == url_clound:
            sheet1 = wbk.add_sheet(u'云资产扫描结果', cell_overwrite_ok=True)
            row0 = [u'业务', u'负责人', u'外网IP', u'内网IP', u'操作系统', u'扫描结果'] 
            for x in xrange(len(row0)):
                sheet1.write(0, x, row0[x], set_style('Times New Roman',220,True))
            for i in xrange(len(result)):
                conn = paramiko.SSHClient()
                conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    conn.connect(hostname = result[i]['WIp'], username = 'root', timeout = 1)
                    stdin, stdout, stderr = conn.exec_command("iptables -nvL|grep -E '10.0.0.0/8|10.12.0.0/16'")
                    cdt = stdout.readlines()
                    ret = ''.join(cdt)
                except:
                    ret = u'无法连接'
                contl = [result[i]['Name'], result[i]['Responser'], result[i]['WIp'], result[i]['LIp'], result[i]['os'], ret]
                for j in xrange(len(contl)):
                    sheet1.write(i+1, j, contl[j])
        elif url == url_idc:
            sheet2 = wbk.add_sheet(u'物理机扫描结果', cell_overwrite_ok=True)
            row0 = [u'项目', u'负责人', u'外网IP', u'内网IP', u'操作系统', u'扫描结果'] 
            for x in xrange(len(row0)):
                sheet2.write(0, x, row0[x], set_style('Times New Roman',220,True))
            for i in xrange(len(result)):
                conn = paramiko.SSHClient()
                conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    conn.connect(hostname = result[i]['wIp'], username = 'root', timeout = 1)
                    stdin, stdout, stderr = conn.exec_command("iptables -nvL|grep -E '10.0.0.0/8|10.12.0.0/16'")
                    cdt = stdout.readlines()
                    ret = ''.join(cdt)
                except:
                    ret = u'无法连接'
                contl = [result[i]['Name'], result[i]['Owner'], result[i]['wIp'], result[i]['lIp'], result[i]['os'], ret]
                for j in xrange(len(contl)):
                    sheet2.write(i+1, j, contl[j])
        else:
            return 'URL is Error !!!'
    wbk.save('checkseal_{0}.xls'.format(Tm))


if __name__ == "__main__":
    WriteDateExcel()


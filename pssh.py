#!/usr/bin/env python3
# _*_coding:utf8_*_
import sys
import paramiko
import getpass
import threading
import os

def ssh_hosts(hosts, cmd, pwd, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=hosts,
        username='root',
        port=port,
        password=pwd
    )
    stdin,stdout,stderr = ssh.exec_command(cmd)
    out = stdout.read()
    error = stderr.read()
    if error:
        print('\033[31;1m[%s]ERROR:\033[0m'%hosts)
        print(error.decode('utf8'),end='')
    if out:
        print('\033[34;1m[%s]OUT:\033[0m'%hosts)
        print(out.decode('utf8'),end='')

    ssh.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s ipaddr_file "commend"' % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file:',sys.argv[1])
        exit(2)
    fname = sys.argv[1]
    cmd = sys.argv[2]
    password = getpass.getpass('Password:')
    with open(fname) as fobj:
        ips = [line.strip() for line in fobj]
    for ip in ips:
        t = threading.Thread(target=ssh_hosts,args=(ip,cmd,password,22))
        t.start()

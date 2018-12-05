import subprocess
import os

def ping(host):
    rc = subprocess.call('ping -c2 %s &> /dev/null' % host,shell=True)
    # rc = 程序运行完成的返回值，等于$?
    if not rc:
        print('%s is up.' % host)
    # else:
    #     print('%s is down.'%host)
if __name__ == '__main__':
    iplist=['192.168.31.%s' % i for i in range(1,255)]
    for ip in iplist:
        pid = os.fork()
        if not pid:
            ping(ip)
            exit()

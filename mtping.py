import threading
import subprocess

class Ping:
    def __init__(self,host):
        self.host=host

    def __call__(self):  #调用实例时执行
        s= subprocess.call('ping -c2 %s &>/dev/null'% self.host,shell=True)
        if s:
            print('%s is down'%self.host)
        else:
            print('%s is up'%self.host)

if __name__ == '__main__':
    ips=('192.168.31.%s' % i for i in range(1,255))
    # ()创建生成器，不占内存，[]创建列表，占用内存空间
    for ip in ips:
        t = threading.Thread(target=Ping(ip)) #创建Ping的实例
        t.start()   #target()  调用


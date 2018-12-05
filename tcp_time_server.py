import socket
from time import strftime
import os


class TcpTimeServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self, c_sock):
        while True:
            data = c_sock.recv(1024)
            if data.strip() == b'exit':
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode('utf8'))
            c_sock.send(data.encode('utf8'))

    def mainloop(self):
        while True:
            cli_sock, cli_addr = self.serv.accept()
            pid = os.fork()
            if pid:
                cli_sock.close()
                while True:
                #client退出时会产生一个僵尸进程，当有新client链接进来时开始处理僵尸进程
                    pid=os.waitpid(-1,1)[0]  #有多个进程时总是优先处理僵尸进程
                    if pid == 0:
                        break
            else:
                self.serv.close()
                self.chat(cli_sock)
                exit()
        self.serv.close()


if __name__ == '__main__':
    s = TcpTimeServer()
    s.mainloop()

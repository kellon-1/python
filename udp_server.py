import socket
import time

host = ''
port = 23456
addr = (host,port)

s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)

while True:
    data , cli_addr = s.recvfrom(1024)
    data = '[%s] %s' % (time.strftime('%H:%M:%S'),data.decode('utf8'))
    s.sendto(data.encode('utf8'),cli_addr)

s.close()

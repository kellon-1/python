import socket

addr = ('192.168.4.254',23456)

c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = input('#: ')
    if data.strip() == 'exit':
        break
    c.sendto(data.encode('utf8'),addr)
    print(c.recvfrom(1024)[0].decode('utf8'))

c.close()

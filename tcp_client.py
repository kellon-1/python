import socket

host = '192.168.4.254'  #服务器ip
port = 23456            #服务器端口
addr = (host,port)

c = socket.socket()  #基于TCP的套结字
c.connect(addr)      #连接服务器
print('Connect to server:',addr)
while True:
    data = input('Clinet: ') + '\t\n'
    c.send(data.encode('utf8'))
    if data.strip() == 'end':
        break
    data = c.recv(1024)
    print('Server:',data.decode('utf8'),end='')
c.close()

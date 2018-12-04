import socket

host = ''           #监听本机所有地址 0.0.0.0
port = 23456        #应该大于1024
addr = (host,port)  #程序的地址:端口号
s = socket.socket() #默认值就是基于TCP的网络套接字

#设置选项,程序结束之后可以端口立即再运行, 不设置此项,默认要等60秒再运行
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)        #绑定地址到套接字
s.listen(1)         #启动一个监听进程
while True:
    cli_sock, cli_addr = s.accept() #等待客户端连接
    print('Client connect from:', cli_addr)
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'end':
            break
        print('Client:',data.decode('utf8'),end='') # bytes 类型转为string 类型
        data = input('Server: ')+'\t\n'
        cli_sock.send(data.encode('utf8')) # string 类型转为bytes类型
    cli_sock.close()
s.close()

#这个程序单进程单线称 只能一边发一次

#yum install -y telnet
# telnet 127.0.0.1 23456
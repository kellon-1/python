#!/usr/bin/env python3
# _*_coding:utf8_*_
import paramiko

ssh = paramiko.SSHClient()   # 创建实例
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 初次ssh时的确认 yes

ssh.connect(
    hostname='127.0.0.1',
    username='root',
    password='Taren1'
)

s = ssh.exec_command('ls /home')   # 执行linux命令
# s返回的是由类文件对象组成的列表,共三项,标准输入,标准输出,标准错误
print(len(s))
out = s[1].read()
error = s[2].read()
print(out.decode('utf8'))
if not error:
    print('执行成功')

ssh.close()
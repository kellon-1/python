#!/usr/bin/env python3
# _*_coding:utf8_*_
from getpass import getpass
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

def send_email(e_host,sender,pwd,recivers,subject,msg):
    message = MIMEText(msg,'plain','utf8')
    message['From'] = Header(sender,'utf8')
    message['to'] = Header(recivers[0],'utf8')
    message['Subject'] = Header(subject,'utf8')
    smtp = SMTP(e_host)
    smtp.login(sender,pwd)
    smtp.sendmail(sender,recivers,message.as_string())

if __name__ == '__main__':
    e_host = 'smtp.126.com'
    sender = 'huangjingpy@126.com'
    pwd = getpass()
    recivers = ['huangjingpy@126.com']
    subject = '邮件测试'
    msg = 'Python 邮件测试\r\n'
    send_email(e_host,sender,pwd,recivers,subject,msg)


'''sina邮箱用密码登陆,126邮箱等其他需要授权码的用授权码登陆'''

'''新浪邮件服务器有个验证要求：http://blog.sina.com.cn/s/blog_4bea75720102x29a.html
所以msg[‘From’]的内容要与发件人保持一致，
可能新浪在检查一致性时，判断过于简单，msg[‘From’]的Header不能添加第2个参数”utf-8”，否则检查不能通过
'''
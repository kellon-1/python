#!/usr/bin/env python3
# _*_coding:utf8_*_
import smtplib
from email.mime.text import MIMEText
from email.header import Header

message = MIMEText('Python邮件测试\n','plain','utf8')
message['From'] = Header('root@localhost','utf8')
message['To'] = Header('bob@localhost','utf8')
message['Subject'] = Header('mail test','utf8')

sender = 'root@redhat.com'
receivers = ['bob@localhost','kellon_py@sina.com','280753699@qq.com']
smtp_obj = smtplib.SMTP('localhost')
smtp_obj.sendmail(sender,receivers,message.as_string())
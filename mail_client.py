
import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.sina.com'
mail_user = 'kellon_py@sina.com'
mail_pwd = getpass()
message = MIMEText('Python邮件测试\n','plain','utf8')
message['From'] = Header('kellon_py@sina.com')
message['To'] = Header('kellon_py@sina.com','utf8')
message['Subject'] = Header('Python mail test','utf8')

sender = 'kellon_py@sina.com'
receivers = ['kellon_py@sina.com','huangjingpy@126.com']
smtp_obj = smtplib.SMTP(mail_host)
smtp_obj.connect(mail_host)
smtp_obj.login(mail_user,mail_pwd)
smtp_obj.sendmail(sender,receivers,message.as_string())
#!/usr/bin/env python3
# _*_coding:utf8_*_
import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'tedu.cn',
    db = 'tedu',
    charset = 'utf8'
)

cursor = conn.cursor()
select1 = "select * from departments"
cursor.execute(select1)
cursor.scroll(1)  # 默认相对位置移动，
result = cursor.fetchone()
print(result)
print('-'* 30)
cursor.scroll(0,mode='absolute') #   绝对路径移动，从头开始
result = cursor.fetchmany(2)
print(result)
print('-' *30)
cursor.scroll(0,mode='absolute')
result = cursor.fetchall()
print(result)

#!/usr/bin/env python3
# _*_coding:utf8_*_
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='tedu.cn',
    db='tedu',
    charset='utf8'
)

cursor = conn.cursor() #创建游标
insert1 = 'INSERT INTO departments(dep_id,dep_name) VALUES(%s,%s)'
#result = cursor.execute(insert1,(1,"人事部"))
data = [(2,'运维部'),(3,'开发部')]
result =cursor.executemany(insert1,data)
conn.commit()
cursor.close()
conn.close()

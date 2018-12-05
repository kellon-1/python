#!/usr/bin/env python3
# _*_coding:utf8_*_
import pymysql

conn=pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'tedu.cn',
    db = 'tedu',
    charset = 'utf8'
)

cursor = conn.cursor()
update1 = "UPDATE departments SET dep_name=%s WHERE dep_name=%s"
cursor.execute(update1,('人力资源部','人事部'))

# delete1 = "DELETE FROM tedu.departments WHERE dep_id=%s"
# cursor.execute(delete1,3)

conn.commit()
cursor.close()
conn.close()
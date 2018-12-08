#!/usr/bin/env python3
# _*_coding:utf8_*_
from dbconn import Employees, Session

kellon = Employees(emp_id=1, name='黄', gender='男', phone='15998998558', email='88878788@qq.com', dep_id=3)
moly = Employees(emp_id=2, name='moly', gender='女', phone='12345432423', email='ml@tedu.com', dep_id=1)
xl = Employees(emp_id=3, name='小李', gender='男', phone='15989779800', email='280099@tedu.com', dep_id=3)
kn = Employees(emp_id=4, name='柯南', gender='男', phone='10000000000', email='666@123.com', dep_id=2)
ds = Employees(emp_id=5, name='德斯', gender='男', phone='18923745193', email='ooxx@wn.com', dep_id=2)
nd = Employees(emp_id=6, name='牛顿', gender='女', phone='10438201348', email='dd@sina.com', dep_id=4)
te = Employees(emp_id=7, name='test',gender='fale',phone='12345678910', email='123@qq.com',dep_id=1)
emps1 = [kellon, moly]
emps2 = [kn, ds, nd]

session = Session()
session.add(te)
session.add(xl)
session.add_all(emps1)
session.add_all(emps2)
session.commit()
session.close()

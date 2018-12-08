#!/usr/bin/env python3
# _*_coding:utf8_*_
from dbconn import Departments,Salary,Employees,Session
from sqlalchemy import and_,or_

session = Session()
# order_by 排序
# qset = session.query(Departments).order_by(Departments.dep_id) #排序
# print(qset)   #qset 此时只是一条SQL语句
# for dep in qset:   #向qset取值时,返回一个个实例
#     # print(dep)
#     print('%s:%s'%(dep.dep_id,dep.dep_name))

# qset = session.query(Employees.name,Employees.phone)
# for name, phone in qset:  # qset 返回的是元组
#     print('%s:%s'%(name,phone))

# qset = session.query(Departments.dep_name.label('部门'))
# # print(qset)  # 等同于 select dep_name AS '部门' from departments;
# for row in qset:
#     print(row.部门)

# 排序,切片   mysql里的limit[3:6]
# qset = session.query(Employees.name,Employees.email).\
#     order_by(Employees.emp_id)[3:6]
#     # qset 因为切片的原因,已经是元组组成列表了,不再是SQL语句
# print(qset)

# filter 过滤
# qset = session.query(Employees.name).filter(Employees.dep_id==2).\
#     filter(Employees.gender=='男')
# print(qset)
# for name in qset:
#     print(name)
#     print('%s'%name)

# and_   or_  条件判断
# qset = session.query(Employees.name).filter(and_(Employees.dep_id==2,Employees.gender=='男'))
# print(qset)
# for name in qset:
#     print(name)

# qset = session.query(Employees.name).filter(or_(Employees.dep_id==2,Employees.gender=='女'))
# for name in qset:
#     print(name)

# qset = session.query(Employees.name,Employees.phone)
# print(qset.all())   #返回列表
# print(qset.first())  #返回满足条件的第一个值

# qset = session.query(Employees.name,Employees.gender).filter(Employees.emp_id==2)
# print(qset.scalar())
# print(qset.one())     #查询结果必须只有一项,否则报错
# print(qset.scalar())  #调用one,返回第一列的值

# 统计
# qset = session.query(Employees)
# print(qset.count())

#聚合,多表查询 :join 要写查询第二参数的表,否则报错
# qset = session.query(Employees.name,Departments.dep_name).\
#     join(Departments,Employees.dep_id==Departments.dep_id)
# print(qset.all())
# print(qset.first())

session.close()
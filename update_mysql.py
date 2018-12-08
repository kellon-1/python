#!/usr/bin/env python3
# _*_coding:utf8_*_
from dbconn import Departments,Session

session = Session()

# 更新
# qset = session.query(Departments).get(1)
# # get(1)  只会查询主键   查询主键是1的记录
# qset.dep_name = '人事部'

qset = session.query(Departments).filter(Departments.dep_id==2)
qset.update({Departments.dep_name:'运维部'})

qset= session.query(Departments.dep_id,Departments.dep_name)
for id,name in qset:
    print(id,name)


session.commit()
session.close()
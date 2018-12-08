#!/usr/bin/env python3
# _*_coding:utf8_*_
from dbconn import Session,Departments

# cw = Departments(dep_id=5,dep_name='cw')
session = Session()

det = session.query(Departments).get(5)
session.delete(det)

# qset = session.query(Departments.dep_id,Departments.dep_name)
# for id , name in qset:
#     print(id,name)

# session.add(cw)
session.commit()
session.close()
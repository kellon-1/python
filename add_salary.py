#!/usr/bin/env python3
# _*_coding:utf8_*_
from dbconn import Salary,Session

jian2018_10 = Salary(
    date = '2018-1-10',
    emp_id = 1,
    basic = 15000,
    awards = 3000
)

jian2018_11 = Salary(
    date = '2018-1-11',
    emp_id = 1,
    basic = 26000,
    awards = 8000
)
moly2018_10 = Salary(
    date = '2018-1-10',
    emp_id = 2,
    basic = 28000,
    awards = 10000
)

moly2018_11 = Salary(
    date = '2018-1-11',
    emp_id = 2,
    basic = 36000,
    awards = 8000
)
jian = [jian2018_11,jian2018_10]
moly = [moly2018_10,moly2018_11]

session = Session()
session.add_all(jian)
session.add_all(moly)
session.commit()
session.close()
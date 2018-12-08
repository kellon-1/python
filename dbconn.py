#!/usr/bin/env python3
# _*_coding:utf8_*_
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建链接数据库的引擎
engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena?charset=utf8',
    encoding='utf8', #echo=True

    # mysql+链接模块://用户：密码@数据库主机/库
)

Base = declarative_base()
Session = sessionmaker(bind=engine)


# 跟服务器通信需要一个会话,通过session 跟引擎绑定, 才能增删改查

class Departments(Base):  # 必须继承于Base
    __tablename__ = 'departments'  # 库中的表名
    # 每个属性都是表中的一个字段，是类属性
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), nullable=False, unique=True)

    def __str__(self):
        return '[部门编号:%s, 部门名字:%s]' % (self.dep_id, self.dep_name)


class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(6))
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return 'ID:%s 员工:%s' % (self.emp_id, self.name)


class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

    def __str__(self):
        return 'Date:%s Name:%s ' % (self.date, self.emp_name)


if __name__ == '__main__':
    # 在数据库中创建表，如果库中已有同名的表，将不会创建
    Base.metadata.create_all(engine)

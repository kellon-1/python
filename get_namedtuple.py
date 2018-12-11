from collections import namedtuple

user = namedtuple('user',['name','age','email'])
tom = user('tom',25,'tom@tedu.cn')
print(tom.name)
print(tom[0])
# 命名元组,可用下标,可用key 取值
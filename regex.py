import re
#对象    返回对象将有方法, m.group() 显示对象m的值

m = re.match('f..','food') # 在开头查找,匹配成功返回对象
m.group()  #对象的值
m = re.match('f..','seafood') # 没有匹配到,返回None

m = re.search('f..','seafood is food') # 在字符串中查找正则模式的第一次出现,返回对象

m = re.findall('f..','seafood is food') # 查找所以的匹配,返回一个列表
print(m)

m = re.finditer('f..','seafood is foods') #返回匹配对象的迭代器
for i in m:
    print(i.group())   #从迭代器中逐个取出匹配对象

result=re.sub('f..','abc','fish is food') #把匹配正则的地方替换成新字符串
print(result)
result=re.split('\.|-','hello-word.tar.gz') #从匹配正则的地方分割字符串
print(result)

patt = re.compile('f..')  #先把要匹配的模式编译,大量匹配时可以提升效率
m = patt.search('fish is food')
print(m.group())


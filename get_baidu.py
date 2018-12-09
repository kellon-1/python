#!/usr/bin/env python3
# _*_coding:utf8_*_
import requests
playload = {'wd':'python'}
r = requests.get('http://www.baidu.com',params=playload)
r.encoding='utf8'

with open('/opt/baidu.html','w') as fobj:
    fobj.write(r.text) #r.text 返回str类型,适用于文本

with open('/opt/baidu2.html','wb') as fobj:
    fobj.write(r.content) #r.content 返回byte类型,适用于二进制格式,图片

    #r.json()   适用于各种数据对象
    #r.headers  返回以字典输出的服务器响应头
    #r.status_code 返回响应状态码



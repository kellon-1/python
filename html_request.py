#!/usr/bin/env python3
# _*_coding:utf8_*_
import requests

playload = {'wd':'hello world'}
r = requests.get('http://www.baidu.com/s',params=playload)

data = r.content
with open('/opt/web1.html','wb') as fobj:
    fobj.write(data)
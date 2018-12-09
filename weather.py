#!/usr/bin/env python3
# _*_coding:utf8_*_
import json
from urllib.request import urlopen

html = urlopen('http://www.weather.com.cn/data/sk/101280101.html')
data = html.read()
html.close()
print(json.loads(data))


html = urlopen('http://www.weather.com.cn/data/cityinfo/101280101.html')
data = html.read()
html.close()
print(json.loads(data))

html = urlopen('http://www.weather.com.cn/data/zs/101280101.html')
data = html.read()
zs = json.loads(data)
html.close()
print(zs['zs']['gj_des'])


#实况天气获取:'http://www.weather.com.cn/data/sk/城市代码.html'
#城市信息获取:'http://www.weather.com.cn/data/cityinfo/城市代码.html'
#详细指数获取:'http://www.weather.com.cn/data/zs/城市代码.html'

#城市代码: weather_city_code.txt

#天气图片位置 c0 替换为相应的图片代码
#http://m.weather.com.cn/img/c0.gif
#http://m.weather.com.cn/img/b0.gif
#http://www.weather.com.cn/m/i/weatherpic/29x20/d0.gif

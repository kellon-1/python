#!/usr/bin/env python3
# _*_coding:utf8_*_
import json
from urllib.request import urlopen

def weather(cityid):
    cityid = cityid +'.html'
    ct = urlopen('http://www.weather.com.cn/data/cityinfo/' + cityid)
    zs = urlopen('http://www.weather.com.cn/data/zs/' + cityid)
    ct_data = json.loads(ct.read())
    zs_data = json.loads(zs.read())
    ct.close()
    zs.close()
    print('实时天气信息:')
    print('\033[34;1m%-10s\033[0m%s' % ('城市',ct_data['weatherinfo']['city']))
    print('\033[34;1m%-10s\033[0m%s' % ('时间',ct_data['weatherinfo']['ptime']))
    print('\033[34;1m%-10s\033[0m%s' % ('天气',ct_data['weatherinfo']['weather']))
    print('\033[34;1m%-10s\033[0m%s ~ %s\n' % ('温度',ct_data['weatherinfo']['temp1'],ct_data['weatherinfo']['temp2']))
    print('\033[34;1m%-7s\033[0m%s\n' % ('舒适度指数',zs_data['zs']['co_des']))
    print('\033[34;1m%-8s\033[0m%s\n' % ('穿衣指数',zs_data['zs']['ct_des']))
    print('\033[34;1m%-8s\033[0m%s\n' % ('防晒指数',zs_data['zs']['fs_des']))
    print('\033[34;1m%-8s\033[0m%s\n' % ('化妆指数',zs_data['zs']['pp_des']))
    print('\033[34;1m%-8s\033[0m%s\n' % ('约会指数',zs_data['zs']['yh_des']))

if __name__ == '__main__':
    city = input('请输入查询城市:')
    with open('weather_city_code.txt') as fobj:
        data = fobj.readlines()
        for line in data:
            if city in line:
                cityid = line.split('=')[0]
                weather(cityid)
                break
        else:
            print('查不到该城市%s' % city)







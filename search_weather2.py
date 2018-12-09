#!/usr/bin/env python3
# _*_coding:utf8_*_
import json
import requests
from time import strftime
def get_weather(cityid,city):
    '''查询城市的时时天气和天气指数'''
    #天气预报,调用和风天气api接口 注册帐号得到key
    url = 'https://free-api.heweather.com/v5/weather?city=' + cityid +'&key=8a439a7e0e034cdcb4122c918f55e5f3'
    weather = requests.get(url)
    weather.encoding = 'utf8'
    data = weather.json()
    wt = data["HeWeather5"][0]['daily_forecast'] #取出天气
    zs = data["HeWeather5"][0]['suggestion']  #取出生活指数
    now = data["HeWeather5"][0]['now']
    ntime = strftime('%H:%M')
    print('\033[31;1m%s\t%s\t%s\t%s度\033[0m' % (city,ntime,now['cond']['txt'],now['tmp']))
    print()
    print('\033[31;1m%-4s\033[0m\t\033[34;1m%-4s\033[0m' % ('空气', zs['air']['brf']),end='')
    print('\t %s' % zs['air']['txt'])
    print('\033[31;1m%-4s\033[0m\t\033[34;1m%-4s\033[0m' % ('舒适度',zs['comf']['brf']),end='')
    print(' %s' % zs['comf']['txt'])
    print('\033[31;1m%-4s\033[0m\t\033[34;1m%-4s\033[0m' % ('穿衣',zs['drsg']['brf']),end='')
    print('\t %s' % zs['drsg']['txt'])
    print('\033[31;1m%-4s\033[0m\t\033[34;1m%-4s\033[0m' % ('感冒',zs['flu']['brf']),end='')
    print('  %s' % zs['flu']['txt'])
    print('\033[31;1m%-4s\033[0m\t\033[34;1m%-4s\033[0m' % ('紫外线',zs['uv']['brf']),end='')
    print('\t %s' % zs['uv']['txt'])
    print()
    print('明天\t%s' % (wt[1]['cond']['txt_d']))
    print('后天\t%s' % (wt[2]['cond']['txt_d']))

if __name__ == '__main__':
    with open('city_code_hefeng.txt') as fobj:
        data = fobj.readlines()
        while True:
            try:
                city = input('请输入查询城市:')
            except (KeyboardInterrupt,EOFError):
                print('\nBye~')
                break
            for line in data:
                cityinfo = line.split(',')
                if city == cityinfo[2]:
                    get_weather(cityinfo[0],city)
                    break

            else:
                print('查不到该城市:%s' % city)
                continue
            break







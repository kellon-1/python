#!/usr/bin/env python3
# _*_coding:utf8_*_

'''获取zabbix版本信息 data从官方网站获得
https://www.zabbix.com/documentation/4.0/zh/manual/api/reference/apiinfo/version
客户端和api之间的请求和响应都用json格式编码
data格式从zabbix官网api里面获取'''

import requests
import json

url = 'http://192.168.1.78/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
}

r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())
#!/usr/bin/env python3
# _*_coding:utf8_*_

import requests
import json
'''获取登陆身份令牌'''
url = 'http://192.168.1.78/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}

r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())
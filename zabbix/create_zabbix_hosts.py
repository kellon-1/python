#!/usr/bin/env python3
# _*_coding:utf8_*_

import requests
import json

url = 'http://192.168.1.78/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Python Linux server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.111",
                "dns": "8.8.8.8",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
    },
    "auth": "ba76215a31dd749537099ba828f290cb",
    "id": 1
}

for i in range(100,111):
    data['params']['host'] = 'Python Linux server%s'%i
    data['params']['interfaces'][0]['ip'] = '192.168.1.%s'%i
    r = requests.post(url,headers=headers,data=json.dumps(data))
    print(r.json())
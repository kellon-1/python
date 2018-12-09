#!/usr/bin/env python3
# _*_coding:utf8_*_

import requests
import json

url = 'http://192.168.1.78/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid","host"],   #output是query 可以进一步查询hostid,host
        "selectInterfaces": ["interfaceid","ip","dns"]
    },
    "auth": "ba76215a31dd749537099ba828f290cb",
    "id": 1
}
r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())
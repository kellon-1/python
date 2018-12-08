#!/usr/bin/env python3
# _*_coding:utf8_*_
import sys
from urllib.request import urlopen
from urllib.error import HTTPError

def get_web(url,fname):
    try:
        html = urlopen(url)
    except HTTPError as error:  #把异常的说明字符串保存到变量error中
        print(error)    #error 返回的是实例的属性,查看源码, error.code 表示状态码,typr(error.code)查看类型是什么
        if error.code == 403:
            print('权限不足')
        elif error.code ==404:
            print('没有那个地址')
        return

    with open(fname,'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

    html.close()

if __name__ == '__main__':
    get_web(sys.argv[1],sys.argv[2])

#!/usr/bin/env python3
# import os
# def g_fname():
#     while True:
#         fname=input("input filename:")
#         if not os.path.exists(fname):
#             break
#     return fname
#
#
# def g_content():
#     content=[]
#     print('input data,write "end" to exit')
#     while True:
#         data=input()
#         if data == 'end':
#             break
#         content.append(data)
#     return content
#
#
# def wfile(fname,content):
#     with open(fname,'w') as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname=g_fname()
#     content=g_content()
#     content=['%s\n' % line for line in content]
#     wfile(fname,content)
import sys
a=sys.argv[1]
print(a)
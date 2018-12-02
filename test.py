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

def pmenu():
    print('#' * 50)
    print('#%-46s#'%('(1) 查询'))
    print('#%-46s#'%('(2) 压栈'))
    print('#%-46s#'%('(3) 出栈'))
    print('#%-46s#'%('(4) 退出'))
    print('#' * 50)
pmenu()
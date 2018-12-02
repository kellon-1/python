#!/usr/bin/env python3
"this module is help you write datas to a new file"
import os


def get_fname():
    while True:
        newfile = input('please input your filename:')
        if not os.path.exists(newfile):
            break
        print('%s already exists.Try again' % newfile)
    return newfile


def get_content():
    content = []
    print('please input data , write "end" to exit! ')
    while True:
        line = input('>')
        if line == 'end':
            break
        content.append(line)
    return content


def wfile(fname, content):
    with open(fname,'w') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname, content)

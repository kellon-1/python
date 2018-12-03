import tkinter
from functools import partial

def hello(word):
    def welcome():
        lb.config(text='hello %s' % word)
    return welcome   #hellon函数返回值是welcome函数

root = tkinter.Tk()
lb = tkinter.Label(text="Hello world!",font='Times 24')
MyBtn = partial(tkinter.Button, root, fg='white', bg='red')
b1 = MyBtn(text='Button 1',command=hello('China'))
b2 = MyBtn(text='Button 2',command=hello('kellon'))
b3 = MyBtn(text='Button 3', command=root.quit)
lb.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()

# 依赖包  yum install -y tk-devel tcl-devel sqlite-devel
# python 编译
# ./configure --prefix=/usr/local
# make && make install

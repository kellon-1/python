from functools import partial

def foo(a,b,c,d):
    return a+b+c+d

if __name__ == '__main__':
    #partial 偏函数,适用于前面几个参数不变，后面参数变化的函数
    print(foo(10,20,30,4))
    print(foo(10,20,30,6))
    add = partial(foo,a=10,b=20,c=30)
    print(add(d=8))
    add2 =  partial(foo,10,20,30)
    print(add2(d=10))
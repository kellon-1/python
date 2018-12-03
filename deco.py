def color(func):   # 此处func参数传入的是一个函数
    def red():
        return '\033[31;1m%s\033[0m' % func()   #此处应该传入func函数执行的结果
    return red       #返回一个函数

def hello():
    return 'hello world!'

@color        #装饰器写法
def kellon():
    return 'hellon kellon！'

if __name__ == '__main__':
    hello = color(hello)
    # 把hello函数 作为参数，传给color函数，再赋给hello后，  hello是一个color返回的新函数
    # hello的返回值,传递给了color函数中形参执行结果func()
    print(hello())


    print(kellon())  # 装饰器效果等同于上面写法
    # kellon 因为有装饰器，调用时不是调用kellon函数
    # 而是相当于color(kellon)()
    # color(kellon)返回red
    # color(kellon)() 等价于red()





def color(func):   #
    def red(*args):   #表示传入为一个多个参数的元组
        return '\033[31;1m%s\033[0m' % func(*args)
        #函数调用时*args 把元组拆分成多个参数，如果为空，调用时就不传递参数
    return red

@color
def hello(args):
    return 'hello %s!'%args

@color        #装饰器写法
def kellon():
    return 'hellon kellon！'

if __name__ == '__main__':
    print(kellon())
    print(hello('word'))

def func1(*args):   # *args  表示接收的参数数量不固定，返回一个元组
    print(args)

def func2(**kwargs):  # **kwargs  表示接收一个key=value 参数，返回一个字典
    print(kwargs)

def func3(x,y):
    print(x * y)

def func4(name,age):
    print('%s age is %s' % (name,age))

if __name__ == '__main__':
    func1()
    func1(10)
    func1(10,'kellon')
    func2()
    func2(name='kellon',age=27)
    func3(*[4,8])    #函数调用参数前 加*表示拆分后面的列表
    func4(**{'name':'kellon','age':27})   # **表示拆分字典，给函数赋值，key必须跟行参一致
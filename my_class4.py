class A:
    def foo(self):   #调用实例时，总是把实例本身做第一个参数赋值给self
        print('In A foo')
    def hello(self):
        print('A hello')
class B:
    def bar(self):
        print('In B bar')
    def hello(self):
        print('B hello')
class C (A,B):  #继承多个类时，   查找对象时 从下向上，自左向右查询
    pass

if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()
    c.hello()
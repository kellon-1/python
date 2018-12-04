class BearToy:
    def __init__(self, name,color, size):
        # __init__在实例化时自动执行，实例本身做第一个参数传递给self
        # 如下实例调用：self.color = tidy.color       color为第二个参数
        self.name = name # 后面参数可以不与self.name相同
        self.color = color  # 绑定属性到实例
        self.size = size
        # 字符串，列表都是类的实例
        # self.color 实例本身的变量，在实例内任何地方都可以调用self.color

    def sing(self):
        print('balabala...')

    def speak(self):
        print('My name is %s'%self.name)
if __name__ == '__main__':
    tidy = BearToy('Tidy','White', 'large')  # 实例化，调用__init__
    print(tidy.color)
    print(tidy.size)
    tidy.sing()
    tidy.speak()

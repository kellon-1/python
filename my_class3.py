# 派生类：
# 		设计两个相同的类，但是有一些不同的功能，用派生类更合适
#
# 	创建子类：my_class3 只需要在圆括号内写明从哪个父类继承即可

class BearToy:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def sing(self):
        print('lalala.....')


class NewBear(BearToy):  # NewBear 子类 继承 BearToy 父类
    def __init__(self,name,color,size,price):
        #BearToy.__init__(name,color,size)   等同于下面这句，推荐用下面：super从自己的父类继承属性
        super(NewBear,self).__init__(name,color,size)
        self.price = price
    def run(self):
        print('running...')


if __name__ == '__main__':
    b1 = NewBear('venibear', 'yellow', 'middle',188)
    print(b1.name, b1.color, b1.size,b1.price)
    b1.sing()
    b1.run()

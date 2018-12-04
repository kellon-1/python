#
# 组合类属性：
#       1、两个类明显不同
#       2、一个类是另一个类的组件
#    如：类（厂商）和 类（玩具熊）类的属性不一样，厂商是玩具熊的标签
class Vendor:
    def __init__(self,phone,email):
        self.phone = phone
        self.email = email
    def call(self):
        print('calling %s'%self.phone)

class BearToy:
    def __init__(self,color,size,price,phone,email):
        self.color = color
        self.size = size
        self.price = price
        self.vendor = Vendor(phone,email)

if __name__ == '__main__':
    bigbear = BearToy('Brown','Middle',199,4008001234,'kellon@tedu.cn')
    smallbear = BearToy('While','small',88,4008001234,'kellon@tedu.cn')
    print(bigbear.price)
    print(smallbear.color)
    bigbear.vendor.call()
    smallbear.vendor.call()
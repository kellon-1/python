class Date:  #创建Date类
    def __init__(self,year,month,date):  #类属性
        self.year = year
        self.month = month
        self.date = date

    @classmethod #类方法 不用创建实例即可调用
    def create(cls,dstr): #cls 表示类本身
        y,m,d =map(int,dstr.split('-'))
        #map(int,['1998','12','6']) 切割字符串，再转化成int类型返回[1998,12,6]
        return cls(y,m,d)  #返回值给实例

    @staticmethod  #静态方法，用不着类的情况下
    def is_date_valid(dstr):
        y, m, d = map(int, dstr.split('-'))
        return 0<=y<=4000 and 1<=m<=12 and 1<=d<=31

if __name__ == '__main__':
    day = Date.create('1998-12-6')  #创建day实例

    print(day)
    print(day.year,day.month,day.date)

    print(Date.is_date_valid('1998-12-06'))
class Book:
    def __init__(self,title,author,pages):
        #返回字符串实例化类实例时默认会调用的方法
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        #打印、显示实例时调用方法，
        return '<<%s>>' % self.title

    def __call__(self):
        #用于创建可调用的实例
        print('<<%s>> is write by %s' % (self.title,self.author))

if __name__ == '__main__':
    py_book = Book('core python','wysley',800)
    print(py_book)   #调用__str__
    py_book()        #调用__call__
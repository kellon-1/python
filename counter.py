def counter(start=0):
    count=start
    def incr():
        nonlocal count
        count += 1
        return count
    #改变外部函数的值
    return incr

if __name__ == '__main__':
    a=counter() #a,b 是一个函数
    b=counter(10)

    print(a())  #调用函数a  count值+1=1
    print(b())
    print(a())  #继续调用a  count值+1=2
    print(b())
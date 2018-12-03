from random import randint

def func1(x):
    return x % 2

def func2(x):
    return x * 2 + 1

if __name__ == '__main__':
    alist=[randint(1,100) for i in range(10)]
    print(alist)
    #filter要求第一个参数三函数，该函数返回值必须为True和False
    #执行时把alist的每一项作为func1的参数，返回True留下，False忽略
    result1=filter(func1,alist) #filter 高阶函数
    print(list(result1))
    result2=filter(lambda x : x % 2,alist)   #匿名函数,等同于 func1
    print(list(result2))

    #map将第二个参数中的每一项都传递给第一个函数参数进行加工，返回执行结果
    result3=map(func2,alist)
    result4=map(lambda x : x * 2 +1 ,alist)
    print(list(result3))
    print(list(result4))


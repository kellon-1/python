def counter(start=0):
    count=start
    def incr():
        nonlocal count  #申明count引用外层count的值
        count +=1
        return count
    return incr

if __name__ == '__main__':
    print(counter()())
    print(counter(10)())
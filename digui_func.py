def func(n=5):
    if n == 1:
        return n
    return n * func(n-1)

if __name__ == '__main__':
    print(func())
    print(func(8))
    print(func(10))
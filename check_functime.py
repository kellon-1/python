import time

def check_time(func):
    def ch_time():
        start=time.time()
        return func() - start
    return ch_time


@check_time
def func1():
    time.sleep(3)
    end=time.time()
    return end


if __name__ == '__main__':
    print(func1())
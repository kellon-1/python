import threading
import time

def calc():
    result=0
    for i in range(50000001):
        result+=i
    print(result)

if __name__ == '__main__':
    stime=time.time()
    t1 = threading.Thread(target=calc)
    t2 = threading.Thread(target=calc)
    t1.start()
    t2.start()
    t2.join()
    t1.join()
    print(time.time()-stime)

import hashlib
import sys

def check_md5(fname):
    m = hashlib.md5()    #创建一个对象
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)    #读取4k数
            m.update(data)
            if not data:
                break
    return m.hexdigest()

if __name__ == '__main__':
    print(check_md5(sys.argv[1]))
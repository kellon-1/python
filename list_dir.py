import os
import sys

def listfile(path):
    if os.path.isdir(path):
        print(path+':')
        flist = os.listdir(path)
        print(flist)
        for fname in flist:
            fname=os.path.join(path,fname)
            listfile(fname)


if __name__ == '__main__':
    listfile(sys.argv[1])
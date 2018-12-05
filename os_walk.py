import os

for path,fdir,files in os.walk('/opt'):
    for fname in files:
        fname=os.path.join(path,fname)
        print(fname)
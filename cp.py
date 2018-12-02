# import os
# src_fname=input("copy from:")
# dest_fname=input("copy to:")
#
# src_fobj=open(src_fname,'rb')
# dest_fobj=open(dest_fname,'wb')
#
# while True:
#     #一次读取太多浪费内存，建议一次读4096b
#     data=src_fobj.read(4096)
#     if not data:
#         break
#     dest_fobj.write(data)
# src_fobj.close()
# dest_fobj.close()
#
# os.chmod(dest_fname,0o755)

import os,sys
def copy(src_fname,dest_fname):
    src_fobj=open(src_fname,'rb')
    dest_fobj=open(dest_fname,'wb')
    while True:
        data=src_fobj.read(4096)
        if not data:
            break
        dest_fobj.write(data)
    src_fobj.close()
    dest_fobj.close()
copy(sys.argv[1],sys.argv[2])

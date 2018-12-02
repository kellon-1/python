#cp /etc/passwd .
#cp /etc/passwd mima
#vim mima -> 修改mima
import  sys
def diff_file(src_file,dst_file,diff_file):
    #对比两个文件的差异
    with open(src_file) as sobj:
       aset=set(sobj)
    with open(dst_file) as dobj:
        bset=set(dobj)
    with open(diff_file,'w') as newobj:
        newobj.writelines(bset-aset)


if __name__ == '__main__':
    diff_file(sys.argv[1],sys.argv[2],sys.argv[3])
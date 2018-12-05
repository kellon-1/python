import os
from time import strftime
import tarfile
import hashlib
import pickle


class Backup:
    def __init__(self, spath, dpath):
        if not os.path.isdir(dpath):
            os.mkdir(dpath)
        fname = os.path.basename(spath).strip('/')
        self.spath = spath
        self.dpath = os.path.join(dpath, fname)
        self.md5name = os.path.join(dpath, 'md5.data')
        self.full_bkname = os.path.join(dpath,'%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d')))
        self.incr_bkname = os.path.join(dpath,'%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d')))

    def check_md5(self, fname):
        m = hashlib.md5()
        with open(fname, 'rb') as fobj:
            while True:
                data = fobj.read(4096)
                if not data:
                    break
                m.update(data)
        return m.hexdigest()


    def fullback(self):
        md5dict = {}
        tar = tarfile.open(self.full_bkname, 'w:gz')  # 打开压缩包,没有则创建
        tar.add(self.spath)  # 把文件目录添加到压缩包
        tar.close()  # 关闭文件

        for path, folders, files in os.walk(self.spath):
            for fname in files:
                fname = os.path.join(path, fname)
                md5dict[fname] = self.check_md5(fname)   #把文件的MD5 写进字典
        with open(self.md5name, 'wb') as fobj:
            pickle.dump(md5dict, fobj)

    def incrback(self):
        md5dict={}
        with open(self.md5name,'rb') as fobj:
           oldmd5=pickle.load(fobj)

        for path,folders,files in os.walk(self.spath):
            for file in files:
                fname = os.path.join(path,file)
                fmd5 = self.check_md5(fname)
                md5dict[fname]=fmd5
        with open(self.md5name,'wb') as fobj:
            pickle.dump(md5dict,fobj)

        tar = tarfile.open(self.incr_bkname, 'w:gz')
        for key in md5dict:
            if md5dict.get(key) != oldmd5.get(key) :
                tar.add(key)
        tar.close()




if __name__ == '__main__':
    bk = Backup('/opt/security', '/opt/backup')
    if strftime('%a') == 'Mon':
        bk.fullback()
    else:
        bk.incrback()
# mkdir /opt/demo
# cp -r /etc/security /opt/demo

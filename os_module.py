import os

os.getcwd()                 # pwd
os.listdir()                # ls -a
os.listdir('/opt')          # ls -a /opt
os.remove('/opt/mydemo/test.txt')     # rm '/opt/test'
os.rmdir('/opt/mydemo')     # rm -rf '/opt/mydemo   只能删除空文件夹
os.mkdir('/opt/mydemo')     # mkdir /opt/mydemo
os.chdir('/opt/mydemo')     # cd /opt/mydemo
os.mknod('test.txt')        # touch test.txt
os.symlink('/etc/hosts','hosts')  # ln -s /etc/hosts hosts
os.path.isfile('test.txt')  #判断test.txt是不是文件
os.path.isdir('/opt')       #判断opt是不是目录
os.path.islink('hosts')     #判断hosts是不是软连接
os.path.exists('test.txt')  #判断是否存在
os.path.basename('/opt/abc/aaa.txt')    #return 'aaa.txt'
os.path.dirname('/opt/abc/aaa.txt')     #return '/opt/abc'
os.path.split('/root/aaa/haha.txt')     #return '/root/aaa','haha.txt'
os.path.join('/home/tom','xyz.txt')     #return  '/home/tom/xyz.txt
os.path.abspath('test.txt')     #返回当前目录下test.txt的绝对路径


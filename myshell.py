import shutil

with open('/etc/passwd', 'rb') as sfobj:
    with open('/tmp/mima.txt', 'wb') as dfobj:
        shutil.copyfileobj(sfobj, dfobj)
        # 流数据拷贝，文件对象obj拷贝，默认第三个参数length省略

shutil.copyfile('/etc/passwd', '/tmp/mima2.txt')
# 将src内容复制到dst文件中

shutil.copy('/etc/shadow', '/tmp/')
# cp /etc/shadow /tmp/

shutil.copy2('/etc/passwd', '/tmp/')
# cp -p /etc/passwd /tmp/

shutil.copytree('/etc/security', '/tmp/anquan')
# cp -r /etc/security    /tmp/anquan   #copy dir and change name

shutil.move('/tmp/mima.txt', '/root/')
# mv /tmp/mima.txt /root/

shutil.rmtree('/tmp/anquan')
# rm -rf '/tmp/anquan'

shutil.copymode('/etc/shadow', '/tmp/mima2.txt')
# 复制/etc/shadow的权限到/tmp/mima2.txt

shutil.copystat('/etc/passwd', '/root/mima.txt')
# 复制src 的元数据（修改时间） shell用stat 查看文件元数据

shutil.chown('/tmp/mima2.txt', user='kellon', group='kellon')
# chown kellon:kellon /tmp/mima2.txt

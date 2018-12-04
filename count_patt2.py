import re
from collections import Counter
#Counter  返回一个Counter 排好序的字典

class CountPatt:
    def __init__(self,fname,):
        self.fname = fname
        #不变的参数,写在类本身属性上

    def count(self,patt):  #变化的参数,在调用类方法的时候传递, 这里是临时参数
        result = Counter()   #
        cpatt = re.compile(patt)

        with open(self.fname) as fobj:
            for line in fobj:
                ip = cpatt.search(line)
                if ip:
                    result.update([ip.group()])
                    #加[]是整体添加,不加[] 把字符串里每一项添加
        return result

if __name__ == '__main__':
    fname = '/opt/access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|Chrome|MSIE'

    result = CountPatt(fname)
    ip_result = result.count(ip)

    print(ip_result)
    print()
    print(ip_result.most_common(3))  #查看value 最大的前三项 返回值是列表
    print()
    print(result.count(br))
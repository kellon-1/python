import os,shutil

def blocks(fobj):
    block = []
    count = 0
    for line in fobj:
        block.append(line)
        count += 1
        if count == 10:
            yield block  #返回中间值，下次取值从这里继续执行
            # yield 返回一个值给blocks函数，block,count归零等待下一次生成值
            block = []
            count = 0
    if block:   #如果yield 返回值后 block无值可取为False
        yield block

if __name__ == '__main__':
    fname='/opt/passwd'
    if not os.path.isfile(fname):
        shutil.copyfile('/etc/passwd',fname)
    fobj=open(fname)
    for lines in blocks(fobj):
    # for 循环直到函数生成器的值 取完才结束，每循环一次yield一次
        print(lines)
        print()
    fobj.close()
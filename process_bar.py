import time, sys


def railway():
    length = 50
    count = 0
    while True:
        print('\r%s@%s' % ('#' * count, '#' * (length - count)), end='')
        # sys.stdout.flush()  #刷新标准输出
        time.sleep(0.1)
        count += 1
        if count == length + 1:
            count = 0


if __name__ == '__main__':
    railway()

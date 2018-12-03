import time, sys


def railway():
    length = 50
    count = 0

    while True:
        print('\r%s@%s' % ('#' * count, '#' * (length - count)), end='')
        # sys.stdout.flush()  #刷新标准输出
        try:
            time.sleep(0.1)
        except (EOFError, KeyboardInterrupt):
            print('\033[31;1m\nBye-bye\033[0m')
            break
        count += 1
        if count == length + 1:
            count = 0


if __name__ == '__main__':
    railway()

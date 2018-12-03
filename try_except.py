try:
    m=int(input('number:'))
    result=100/m
except (ValueError,ZeroDivisionError):
    print('Invalid number.')
except (KeyboardInterrupt,EOFError):
    print('\nBye')
else:   #异常不发生时执行else
    print('\033[31;1m%s\033[1m'%result)
finally:  #不管异常是否发生都执行finally
    print('\033[34;1mDone\033[0m')

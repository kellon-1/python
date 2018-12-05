import os
import time
# print('starting...')
# os.fork()   #生成一个子进程,后面的代码父进程和子进程都会执行一遍
# print('hello world')

# for i in range(2):
#     pid=os.fork()   #父进程返回的是子进程PID号， 子进程返回0
#     if not pid:     # if 为True 子进程执行下面代码，执行结束退出
#         print('hello')
#         exit()      # 如果不退出，在循环里容易引起进程炸弹

pid = os.fork()
if pid:
    # os.waitpid(-1,1) 第一个参数-1 表示与wait()函数相同，
    # 第二个参数0表示挂起父进程，1 表示不挂起父进程（父进程可以一起工作）
    # waitpid()的返回值：如果子进程尚未结束返回0，否则返回子进程的PID，并杀死子进程

    print('In parent. sleeping...')
    print(os.waitpid(-1,1))
    time.sleep(20)
    print(os.waitpid(-1,1))
    time.sleep(40)
    print('parent done')
else:
    print('In child. sleeping...')
    time.sleep(10)
    print('child done')
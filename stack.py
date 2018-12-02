import os

stack = ['test']


def push_it():
    push_data = input("Input:")
    stack.append(push_data)
    print("\033[34;1mPush %s successfully\033[0m" % push_data)


def pop_it():
    if stack:
        print("\033[31;1mPop %s successfully\033[0m" % (stack.pop()))


def check_it():
    print("\033[30;1m%s\033[0m" % stack)


def pmenu():
    cmds = {'1': check_it, '2': push_it, '3': pop_it}
    prompt = '''
##################################################
#(1) 查询                                        #
#(2) 压栈                                        #
#(3) 出栈                                        #
#(4) 退出                                        #
##################################################
请输入[1/2/3/4]:'''
    while True:
        chioce = input(prompt).strip()[0]
        if chioce not in '1234':
            print('Invalid input. Please try again:')
            continue
        if chioce == '4':
            break
        cmds[chioce]()
        # if chioce=='1':
        #     check_it()
        # elif chioce=='2':
        #     push_it()
        # elif chioce=='3':
        #     pop_it()


if __name__ == '__main__':
    pmenu()

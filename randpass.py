import string,random

pass_list = string.ascii_letters + string.digits

#方法1
result=[random.choice(pass_list) for i in range(8)]
print(''.join(result))

#方法2
print(''.join([random.choice(string.digits+string.ascii_letters) for i in range(8)]))

#方法3   调用string模块 大小写字母/特殊符号/数字
def choice_pass(n=8):
    password=''
    for i in range(n):
        password+=random.choice(pass_list)
    return password

#print (choice_pass())
if __name__ == '__main__':
    print(choice_pass())

# if len(sys.argv) == 1:
#     print(choice_pass())
# else:
#     args=int(sys.argv[1])
#     print(choice_pass(args))

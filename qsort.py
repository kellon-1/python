from random import randint

def quick_sort(num_list):
    #num_list.sort(reverse=True)
    if len(num_list) < 2:
        return num_list
    middle=num_list[0]
    min_list=[]
    max_list=[]
    for i in num_list[1:]:
        if i < middle:
            min_list.append(i)
        else:
            max_list.append(i)

    # 递归函数：需要一个结束条件，再找一个中间值递归
    return quick_sort(min_list) + [middle] + quick_sort(max_list)

if __name__ == '__main__':
    alist=[randint(1,100) for i in range(10)]
    print(alist)
    print(quick_sort(alist))

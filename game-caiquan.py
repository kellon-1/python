#!/usr/local/bin/python3
import random
all_choices=['石头','剪刀','布']
winlist=[['石头','剪刀'],['剪刀','布'],['布','石头']]
computer=random.choice(all_choices)
prompt='''(0)石头
(1)剪刀
(2)布
请选择(0/1/2）:'''
ider=int(input(prompt))
if ider not in [0,1,2]:
    print("you must choice 0,1,2")
else:
    player = all_choices[ider]
    print('computer:%s,you:%s'%(computer,player))
    if computer == player :
        print("\033[32;1m平局\033[0m")
    elif [computer,player] in winlist:
        print("\033[30;1mYOU LOSE!\033[0m")
    else:
        print("\033[31;1mYOU WIN!\033[0m")


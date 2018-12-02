#!/usr/bin/env python3
alist=[10,'kellon']
#list(enumerate(alist))   #[(0,10),(1,'kellon')]
#a,b=1,30  #a->1   b->30

for ind in range(len(alist)):
    print('%s:%s'%(ind,alist[ind]))

for item in enumerate(alist):
    print("%s:%s"%(item[0],item[1]))

for ind,val in enumerate(alist):
    print("%s:%s"%(ind,val))

atuple=(29, 92, 12, 80, 29, 13, 38, 17, 27, 82)
print(sorted(atuple))
for i in reversed(atuple):
    print(i,end=',')
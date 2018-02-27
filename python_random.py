# -*- coding=utf-8 -×-
import random
j =  int(input("你想试几次\t"))
k=0
if j>0 and j<=1000000:
    k = j
else:
    print("输入有误，请重试")
i = 1
while i<=k:
    num = int(random.randint(0,1))
    if num == 0:
        print("她爱我\t\t第%d次"%i)
        i+=1
    else:
        print("她不爱我\t第%d次"%i)
        i+=1

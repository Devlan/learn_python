import random
# -*- coding=utf-8 -*-
i = 0
num = int(input("大爷，玩多少次啊\t"))
if num >= 1000000:
    print("找茬啊，滚！")
while i <=num:

    player = int(random.randint(1,6))
    computer = int(random.randint(1,6))
    if computer == player:
        print("电脑是%d,你是%d,平手，再来"%(computer,player))
    elif computer > player:
        print("电脑是%d,你是%d,你输了，菜"%(computer,player))
    else :
        print("电脑是%d,你是%d,你赢了，牛"%(computer,player))
    i+=1

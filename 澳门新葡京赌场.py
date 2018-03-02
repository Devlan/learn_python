# coding: utf-8
import random
def roll_dice(numbers=3, points=None):
    print('<<<<< 美女荷官在线发牌! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers -= 1
    return points
def start_game():    
    money = 1000
    while 1:
        #1.玩家输入Big或small来押大压小
        print('<<<<< 亲，请下注! >>>>>')
        player_choice = raw_input("押大押小: ")
        bet = int(input("亲，您想押多少 ? - "))
        #2.摇三个骰子，计算总和sum
        points = roll_dice()
        sum = points[0] + points[1] + points[2]
        #3.11<=sum<=18为大，3<=sum<=10为小
        result = ''
        if 11<=sum<=18:
            result = '大'
        elif 3<=sum<=10:
            result = '小'
        #4.判断玩家猜对没有
        if player_choice == result:
            money = money + bet
            print('开！结果是%s您赢了!'%points)
            print('您赢了%d块,现在您有%d块'%(bet,money))
        else:
            money = money - bet
            if money <= 0:
                print('开！结果是%s您输了!'%points)
                print('您赔了%d块,现在您有。。。额，穷鬼一毛钱都没有，滚！'%bet)
                print('再见傻逼！')
                break
            print('开！结果是%s您输了!'%points)
            print('您赔了%d块,现在您还有%d块'%(bet,money))
#下注金额和赔率，初始金额为1000,金额为0时结束, 默认赔率为1
'''money = 1000
if money == 0:
    print('GAME OVER')
    break
bet = int(input("How much you wanna bet ? - "))
print('You gained ' + bet + ',you have '+ money + 'now')
print('You lost ' + bet + ',you have ' + money +'now')
'''
start_game()

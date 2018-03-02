# coding: utf-8
import random
def roll_dice(numbers=3, points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
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
        print('<<<<< GAME STARTS! >>>>>')
        player_choice = raw_input("Big or Small: ")
        bet = int(input("How much you wanna bet ? - "))
        #2.摇三个骰子，计算总和sum
        points = roll_dice()
        sum = points[0] + points[1] + points[2]
        #3.11<=sum<=18为大，3<=sum<=10为小
        result = ''
        if 11<=sum<=18:
            result = 'Big'
        elif 3<=sum<=10:
            result = 'Small'
        #4.判断玩家猜对没有
        if player_choice == result:
            money = money + bet
            print('The points are ' + str(points) + "You Win!")
            print('You gained ' + str(bet) + ',you have '+ str(money) + 'now')
        else:
            money = money - bet
            if money <= 0:
                print('The points are ' + str(points) + "You Lose!")
                print('You lost ' + str(bet) + ',you have ' + str(money) + ' now')
                print('GAME OVER')
                break
            print('The points are ' + str(points) + "You Lose!")
            print('You lost ' + str(bet) + ',you have ' + str(money) + 'now')
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

# -*- coding:UTF-8 -*-
amount = float(input("请输入资金数额： "))
rate = float(input("请输入利率： "))
time = int(input("请输入投资时间(整年):  "))
#every_sum_money = 0
#总额=时间*利率*金额+金额
#sum = time * rate * amount + amount
#每年总额=之前总额*利率+之前总额
#next_sum = sum * rate + sum
def invest():
    year_num = 1
    while year_num <= time:
        sum = year_num * rate * amount + amount
        next_sum = sum * rate + sum
        print("第%d年：复利为%f "%(year_num,next_sum))
        year_num += 1
invest()

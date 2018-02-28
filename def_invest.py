# -*- coding:UTF-8 -*-
amount = float(input("请输入资金数额： "))
rate = float(input("请输入利率： "))
time = int(input("请输入投资时间(整年):  "))
year_num = 1
every_sum_money = 0
#第一年=时间*利率*金额+金额
#第二年=第一年*利率+第一年
#n=（n-1）*r+a
#n=n*（r+1）*a（需要把上一年的总额赋给a）
def invest():
    while year_num <= time:
        pass

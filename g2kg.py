#coding:utf-8
def g2kg(g):
    kg = g /1000
    return kg
num = int(input("请输入g数"))
kg = g2kg(num)
print("%dg是%dkg"%(num,kg))


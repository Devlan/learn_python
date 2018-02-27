#coding:utf-8
def xiebian(a,b):
    c = (a*a+b*b) ** 0.5
    print("The right triangle third side's length is %d"%c)
    return c
num1 = int(input("请输入第一条直角边长"))
num2 = int(input("请输入第二条直角边长"))
xiebian(num1,num2)

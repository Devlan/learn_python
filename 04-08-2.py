def sum(a,b,c):
    return a+b+c
def average(a,b,c):
    result = sum(a,b,c)
    result/=3
    print(result)
a = int(input("请输入："))
b = int(input("请输入："))
c = int(input("请输入："))
print(sum(a,b,c))
average(a,b,c)

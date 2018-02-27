# coding: utf-8
def p_excel(name,msg):
    path = '/home/pi/'
    full_path = path+name+'.xls'
    file = open(full_path,'w')
    file.write(msg)
    print('Done')
    
p_excel(考勤表,"小明 迟到30次，没工资，奖金全扣")
p_excel("考勤表","小明 迟到30次，没工资，奖金全扣")
ls
ls /home/pi
more /home/pi/考勤表.xls
def p_excel(name,msg):
    path = '/home/pi/'
    full_path = path+name+'.xls'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
    
30+40
70-40
10%5
10**2
25 **0.5
19//9
19.0//9
type(Ture)
type(True)
type(false)
type(False)
1>2
1<2<3
'Name' == 'name'
'M' in 'Magic'
number = 12
number is 12
1 !=2
1 == 1
middle = 5
1 < middle < 10\
1 < middle < 10
two = 1 + 1
three = 1 + 3
two < three
'Age' == 'age'
abs(-100) > len('udsahuidgh sdfgdkjashfkjhadskfhfasd')
42 > 'the answer'
42 == 'the answer'
42 != 'the answe'
5.0 == 5
3.0 > 1
1 = 1
True > False
True + False > False + False
True
True + True + False
a = []
a.append('11,22,33')
a
type(a)
print(a[0,1])
print(a[0])
del a[0]
a
a.append(11,22)
a.append(22)
a
a.insert(0,11)
a
a.insert(0,11,33)
a.append(44)
a
a.insert(2,33)
a
a.append('55')
a
a.append(True)
a
a[5]
len(a)
print(a[0],a[-1])
False in a
11 in a
66 not in a
11 not in a
the_Eddie = 'Eddie'
name = 'Eddie'
the_Eddie == name
the_Eddie is name
bool(0)
bool(1)
bool([])
bool([1])
bool('')
bool(none)
bool(None)
a_thing = None
not 1
not 0
1 and 0
bool(1 and 0)
bool(not(1 and 0))
1 or 0
1 and 2
1 < 3 and 2 <5
1 < 3 and 2 >5
1<3 or 2>5
1<3 or  2>5
def account_login():
    password = input('Password')
    if password == '12345':
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()
        
account_login()
def account_login(): #定义一个登陆函数
    password = input('Password') #获取并将用户输入的密码存在password变量里
    if password == '12345': #判断用户输入的密码是否正确
        print('Login success!') #正确则打印
    else:
        print('Wrong password or invalid input!') #密码不正确则提示并重新输入
        account_login() #调用登陆函数自身
        
account_login()
password_list = ['*#*#','12345']
def account_login():
    password = input('Password:') #获取输入的密码并传给password
    password_correct = password == password_list[-1] #判断输入的密码与当前密码是否相等，并将bool值赋给password_correct
    password_reset = password == password_list[0]    #判断输入的密码与重置码是否相等，并将bool值赋给password_reset
    if password_correct:#如果密码判断值为真，打印登录成功
        print('Login Success!')
    elif password_reset:#如果重置码判断值为真，修改密码并重新调用自身
        new_password =  input('Please input a new password: ')
        password_list[-1] = new_password
        account_login()
    else:#其他情况就打印密码错误请重试，并调用函数自身
        print('wrong password or invalid input! please try again!')
        account_login()
        
account_login()
account_login()
?save
%save -r ipython_code.py  1-105
ls
more ipython_code.py
%save -r ipython_code.py  1-109

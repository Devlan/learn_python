# -*- coding: UTF-8 -*-
create_txt()
def create_txt():
    file_count = int(input("请输入创建文件数： "))
    file_last_name = input("请输入文件后缀名（ex：.xxx）： ")
    num = 1
    while num <= file_count:
        file_name = str(num) + file_last_name
        file = '/home/pi/' + file_name
        open(file,'w')
        print(file + '已创建!')
        num += 1

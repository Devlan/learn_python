#coding:UTF-8
def copy_file():
    #1.用户输入要复制的文件名
    #python2和python3的input差别：python2视为表达式,python3视为字符串,所以用raw_input
    t_file_name = raw_input("请输入要复制的文件名: ")
    #2.打开要复制的文件
    t_file = open(t_file_name,'r')
    #3.新建文件
    position = t_file_name.rfind('.')
    n_file_name = t_file_name[:position] + '[附件]' + t_file_name[position:]
    n_file = open(n_file_name,'w')
    #4.读原文件
    t_contect = t_file.read()
    #5.将读到的内容写入新文件
    n_file.write(t_contect)
    #6.关闭两个文件
    n_file.close()
    t_file.close()

copy_file()

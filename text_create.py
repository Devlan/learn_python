# -*- coding: UTF-8 -*-

def text_create(name,msg):
    desktop_path = '/home/pi/python_test/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')

def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
    return word .replace(censored_word,changed_word)

def censored_text_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)

censored_text_create('Try','lame!lame!lame!')

text_filter('Python is lame!')
text_create('hello','hello world') # 调用函数

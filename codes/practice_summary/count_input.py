#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
     定义一个函数，可统计出输入任意的字符中英文字母、空格、数字和其它字符的个数
'''
str_in = input("请输入任意字符：")

count_alpha = 0
count_space = 0
count_digit = 0
count_other = 0

for x in str_in:
    if(x.isalpha()):
        count_alpha += 1
    elif(x.isspace()):
        count_space += 1
    elif(x.isdigit()):
        count_digit += 1
    else:
        count_other += 1   

print('中英文个数=%d,空格个数=%d,数字个数=%d,其他字符=%d'%(count_alpha, count_space, count_digit, count_other))


#!/usr/bin/python 

# -*- coding: utf-8 -*-
'''
    有1、2、3、4个数字，能组成多少个互不相同且无重复数字的两位数？都是多少？
'''
num_lst = list(range(1,5))
n = 0
result_lst = []
for x in num_lst:
    for y in num_lst:
        if(x != y):
            n += 1 
            num_add = str(x) + str(y)
            result_lst.append(num_add)
result_lst = list(map(int, result_lst))  #转为数字类型的list
print('互不相同且无重复数字的两位数有:',result_lst,',个数为:%d'%n)
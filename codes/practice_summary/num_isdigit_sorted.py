#!/usr/bin/python 

# -*- coding: utf-8 -*-
'''
输入三个整数x,y,z，请把这三个数由小到大输出，可调用input()。（需要加判断：判断输入数据是否为数字）
'''
def num_sort(n):
    result_lst = []
    for i in range(1,n+1):
        in_str = input('请输入一个整数:')
        while(not (in_str.isdigit())):
            in_str = input('输入有误,请重新输入:')
        result_lst.append(int(in_str))
    return sorted(result_lst)

print(num_sort(3))


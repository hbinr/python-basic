#!/usr/bin/python 

# -*- coding: utf-8 -*-
'''
输入三个整数x,y,z，请把这三个数由小到大输出，可调用input()。（需要加判断：判断输入数据是否为数字）
'''

def num_sort2():
    result_lst = []
    count = 0
    while(count < 3): # 限定比较三个整数
        in_str = input('请输入一个整数:')
        while(not (in_str.isdigit())):
            in_str = input('输入有误,请重新输入:')
        else:
            count += 1
            result_lst.append(int(in_str))
    return sorted(result_lst)
print('三个整数比较后的结果为:',num_sort2())
#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
    创建一个模块，包含一个阶乘函数f1(n)、一个列表删值函数f2(lst,x),一个等差数列求和函数f3(a,d,n)
'''
#阶乘 从1开始乘
def factorial(n):
    result = 1 
    for x in range(1, n+1):
        result *= x
    print('%d的阶乘为:%d' %(n, result))

#列表删值函数 入参为:list,想删的值  
def remove_lst(lst, x):
    # for i in lst:
    #     lst.remove(x)
    # print('删除后的结果为：',lst)
    #
    #不能使用for循环,不知道要循环几次,也不知道什么时候不满足条件才推出
    while(x in lst):
        lst.remove(x)
    print('删除后的结果为：',lst)

def arithmetic_progression_sum(a, d, n):
    an = a
    sum = a
    for x in range(n - 1):
        an += d
        sum += an
    print('首项为%d,公差为%d,项数为%d,等差数列的和为%d' %(a, d, n, sum))
arithmetic_progression_sum(10,5,5)


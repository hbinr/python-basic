#!/usr/bin/python

# -*- coding: utf-8 -*-

'''
    猜数字问题，要求如下：
    ① 随机生成一个整数
    ② 猜一个数字并输入
    ③ 判断是大是小，直到猜正确
    ④ 判断时间
'''
#分析：随机整数，则random.randomint()；输入必须保证是数字才开始比较；判断时间，则需要导入time模块

import random
import time


def verify_num(in_num):
    while(not (in_num.isdigit())):
        in_num = input('输入有误,请重新输入一个数字:')
    else:
        return in_num

i = random.randint(0,100)
in_num = input('Game Start！请输入您猜的数字:')
begin_time = time.time()
in_num = verify_num(in_num)
while(int(in_num) != i):
    if(int(in_num) > i):
        in_num = input('猜错了，请输入更小的一个数字:')
        in_num = verify_num(in_num)
    else:
        in_num = input('猜错了，请输入更大的一个数字:')
        in_num = verify_num(in_num)
end_time = time.time()
print('猜对了，共计用时:',str((end_time - begin_time)) + 'ms')
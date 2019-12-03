#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 8:42
# @Author  : duanhaobin
# @File    : 06_char_sub_split.py
# @Software: PyCharm
# @desc:   re.sub() 和re.split()学习


import re

'''
    1、替换
        re.sub(pattern, repl, string, count=0, flags=0) → 替换字符串中的匹配项
        pattern : 正则中的模式字符串。
        repl : 替换的字符串，也可为一个函数。
        string : 要被查找替换的原始字符串。
        count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
        flags : 编译时用的匹配模式，数字形式
'''
s = 'one Do 334 you want 12 be a super man 11033 2'
print(re.sub(r' ', '', s))  # oneDoyouwantbeasuperman110332 去掉所有空格
print(re.sub(r'\D', '', s))  # 33412110332  提取数字(将所有非数字转换为空字符串)

'''
    2、分割
        re.split(pattern, string[, maxsplit=0, flags=0]) → 按照能够匹配的子串将字符串分割后返回列表
        pattern	匹配的正则表达式
        string	要匹配的字符串。
        maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
        flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
'''
print(re.split(r' ', s))  # ['one', 'Do', '334', 'you', 'want', '12', 'be', 'a', 'super', 'man', '11033', '2']
result = re.split(r'\D+', s)
print(result)  # ['', '334', '12', '11033', '2']  分割出数字
print(''.join(result))  # 33412110332  拼接字符串

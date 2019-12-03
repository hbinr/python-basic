#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 8:07
# @Author  : duanhaobin
# @File    : 05_char_search_findall.py
# @Software: PyCharm
# @desc:   re.search() 和re.findall()学习

import re

'''
    1、re.search(pattern, string, flags=0) → 扫描整个字符串并返回第一个成功的匹配
    参数
        pattern：匹配的正则表达式
        string：要匹配的字符串。
        flags：标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
    返回结果 - 和re.match()一致
        匹配成功re.match方法返回一个匹配的对象，否则返回None。
        可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
        通过span()方法用于以元祖形式返回匹配的起始位置和结束位置
    re.match与re.search的区别
        re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
'''
s = 'one 123 ssdf helo 123  4 34'
result = re.search(r'\d{3}', s)
print(result)  # <re.Match object; span=(4, 7), match='123'>
    # 可以看到结果中只返回了第一个123(返回第一个成功的匹配)
print(result.group())  # 123
print(result.span())  # (4, 7)

result = re.match(r'\d{3}', s)
print(result)  # None  字符串不是以3个数字开头的，所以无法匹配到结果
'''
    2、findall(pattern, string, flags=0) → 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
    参数
        pattern：匹配的正则表达式
        string：要匹配的字符串。
        flags：标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
'''
result = re.findall(r'\d{3}', s)
print(result)  # ['123', '123']  结果返回了所有满足条件的字符串  以列表方式返回


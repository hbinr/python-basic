#!/usr/bin/phthon

# -*- coding: utf-8 -*-

'''
    1. all(iterable)
    对于 all函数，如果可迭代参数的所有元素为真（或迭代器为空）
    版本：该函数在python2.5版本首次出现，适用于2.5以上版本，包括python3，兼容python3版本。
    说明：如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
''' 
lst_one = [1, 23, 0, 2]
print(all(lst_one))    # 输出:False    lst列表中有0

lst_two = [[], (1,2), 1, 2]
print(all(lst_two))    # 输出:False    lst列表中有空列表

# 注意：单个对空元组、空列表为参数时，返回值为True，这里要特别注意

print(all([]))   # True 空列表

print(all(()))   # True 空元组


'''
    2. 对于 any函数，可迭代参数的任何一个元素为真就返回 True，否则返回 False。
    版本：该函数适用于2.5以上版本，兼容python3版本。
    说明：如果iterable的任何元素不为0、''、False,all(iterable)返回True。如果iterable为空，返回False。
'''

tup_one = (1,'s','')
print('any():', any(tup_one))   # any(): True
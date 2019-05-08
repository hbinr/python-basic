#!/usr/bin/python

# -*- coding: utf-8 -*-
'''
    random随机数模块学习

'''
import random

# 1. random() 生成0-1的随机数  [0,1)范围
x = random.random()
y = random.random()
print('0-1随机浮点数:',x, y)

# 2. randint(num1,num2) 随机整数
x = random.randint(1,10)
y = random.randint(1,20)
print('随机整数:',x, y)

# 3. choice(sequence_arg) 随机取样,参数必须为序列,因为是按照索引去选择的
str_one = 'hello world!'
lst = list(range(1000))
x = random.choice(str_one)
y = random.choice(lst)
print('随机取样:',x, y)


# 4. sample(sequence_arg) 随机取指定数量的元素 参数必须为序列,因为是按照索引去选择的
# print(random.sample(5,1))   #报错TypeError: Population must be a sequence or set.  For dicts, use list(d)

x = random.sample(str_one,2)
y = random.sample(lst,5)
print('随机取指定数量的元素:',x, y)


# 5. 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
print('随机数打乱排序后的结果:',items)

# 6. randrange 随机选取[num1,num2)范围内的数字，步长为n

print('随机选取0到10间的偶数:', random.randrange(0, 11, 2))    #随机选取0到10间的偶数 10






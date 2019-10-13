#!/usr/bin/phthon

# -*- coding: utf-8 -*-
'''
    记录Pythonic的写法
    P'即表示'Pythonic'，很 Python 的写法，'NP'也就是相反，不是很'Pythonic'的写法。
'''
# 1.链式比较

a, b = 50, 20
# NP:
0 <= b and b<=a and a< 100
# P:
0 <= b <= a < 100   #写法更接近数学表达式。
print(0 <= b <= a < 100)

# 2. Python里没有Java中的三目运算符，但是可以使用if/else来近似实现

# NP:
age = 19
if age > 18:
    print('adult')
else:
    print('teenager')
# P:
result = 'adult' if age > 18 else 'teenager'

# 3. 字符串列表的连接
lst_str = ['Life', 'is', 'short.','I', 'use', 'Python']
s = ''
# NP:
for i in lst_str:
    s += i + ' '
print(s)
# P:
s = ' '.join(lst_str)
print(s)


# 4.匹配字符串开头/结尾

fname1 = 'python.jpg'

fname2 = 'folwer.bmp'

fname3 = 'readme.txt'

### P:
print(fname1.startswith('python'))            #输出:True

print(fname2.endswith('.jpg'))                #输出:False

print(fname2.endswith(('.jpg', '.bmp')))      #输出:True

print(fname3.endswith(('.jpg', '.bmp')))      #输出:False
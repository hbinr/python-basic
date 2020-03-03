#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    文件读取
    txt存储的时候编码与open()中encoding参数关系:
    txt      encoding
    ANSI  -> 'gbk'
    UTF-8 -> 'utf8'
"""

import os

os.chdir('C:\\Users\\HBlock\\Desktop')  # 切换到桌面

file = open('test.txt', mode='r', encoding='utf8')  # 保证桌面有文件test.txt

# 1. read(size)  返回读取到的size个字符，无参默认全量读取
print(file.read())  # 输出:0123456789开始中文then English
file.seek(0)  # 指针返回0处
print(file.read(10))  # 输出:0123456789
file.seek(0)

# 2. readline(size)  以行为单位读取方法用于从文件读取整行，包括 "\n" 字符。
#                    如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
print(file.readline())
# 输出:
# 0123456789开始中文then English    
#       (不显示,test.txt文件的第一行有换行符)
print(file.readline())
# 输出:987654321第二行 English      (结果中换行符)

file.seek(0)
# 读取一行中的前12个字符
print(file.readline(12))  # 输出:0123456789开始
file.seek(0)

# 3. file.readlines([sizeint])  读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。
result = file.readlines()
print(type(result))  # 输出:<class 'list'>
print(result)  # 输出:['0123456789开始中文then English\n', '987654321第二行 English']

# 遍历一个文件：for语句+f.readlines()
for line in result:
    print(line)

# 4. 练习:读取文件，编写成一个json形式（列表字典）
# [{'name':'...', 'lng':..., 'lat':..., 'address':'...'},{...},...,]
# 经度和纬度英文：longitude and latitude

path_bj_parks = 'F:/WorkSpaces/python-basic/program_data/beijing_park.txt'
file_content = open(path_bj_parks, mode='r', encoding='utf8')
result = []  # 新建一个列表,用来存储数据
n = 0

# 读取每一行数据,遍历来处理输出格式
for line in file_content.readlines():
    n += 1
    str_lst = line.split(':')
    name = str_lst[0]  # 先以:拆分，筛选出name文本
    information = str_lst[1]  # 第二部分包括lng，lat，address
    str_lst_last = information.split(',')
    lng = float(str_lst_last[0])  # 获取经度 并将字符串转为float
    lat = float(str_lst_last[1])  # 获取纬度 并将字符串转为float
    address = str_lst_last[2].strip()  # 获取park地址,去除末尾空格
    data = [['name', name], ['lng', lng], ['lat', lat], ['adress', address]]  # 做成嵌套列表
    result.append(dict(data))

print(result)
print('数据转换成功,共转换%d条数据!' % n)

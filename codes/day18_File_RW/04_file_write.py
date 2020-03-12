#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    文件写入,写入的数据必须是字符串
"""

# 1. write(str) 将字符串写入文件，返回的是写入的字符长度。
path = 'C:/Users/HBlock/Desktop/test_w.txt'
file_w = open(path, 'w', encoding='utf8')  # 先读取该文件,没有则创建一个
file_w.write("文件写入练习 write finished")
# file_w.close()

# 2. writelines(sequence)  向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。无返回值
lst = ['1', '3', '231', 'sdada']
# 如果元素过多,可以给每一元素加入换行符
for i in range(len(lst)):
    lst[i] += '\n'
file_w.writelines(lst)
print("Write finished!")

# 3. 练习:两个列表[1~10],[a~j]，写入一个txt，变成以下格式:
'''
1,a

2,b

3,c
'''

# 分析:两个列表的元素依次相连，用逗号分隔，且有换行
int_lst = list(range(ord('a'), ord('j') + 1))  # 生成ASCII值的列表
alpha_lst = list(map(chr, int_lst))  # chr()ASCII值转成对于的字符

num_lst = list(range(1, 11))
result = []

for i in range(len(num_lst)):
    file_w.writelines([str(num_lst[i]) + ',' + alpha_lst[i] + '\n'])

file_w.close()
print('Write Finished!')

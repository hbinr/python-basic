#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    文件对象声明及基本操作

    另一种数据格式：文件/文档
'''

# 1. 文件路径定义
# 本地文件的界定：指向一个本地存储的文件，是一个链接或者一个映射

path1 = 'C:/Users/HBlock/Desktop/git命令总结.txt'  # 单个反斜杠：/
path2 = 'C:\\Users\\HBlock\\Desktop\\git命令总结.txt'  # 两个斜杠：\\（第一个\是转义符）
path3 = r'C:\Users\HBlock\Desktop\git命令总结.txt'  # r用于防止字符转义
# 路径书写格式
print(path1)    #输出:C:/Users/HBlock/Desktop/git命令总结.txt
print(path2)    #输出:C:\Users\HBlock\Desktop\git命令总结.txt
print(path3)    #输出:C:\Users\HBlock\Desktop\git命令总结.txt 

# 2. 读取文件：open语句
file = open(path1,mode = 'r', encoding = 'utf8')
print(type(file))   #输出:<class '_io.TextIOWrapper'>
print(file)         #输出:<_io.TextIOWrapper name='C:/Users/HBlock/Desktop/git命令总结.txt' mode='r' encoding='utf8'>
print('读取文件,结果为:',file.read())

'''
    open('路径', '模式', enconding = '编码' )
    模式：r：读取文件，默认；w：写入；rw：读取+写入；a：追加
    简答的读取方法：.read() → 读取后，光标将会留在读取末尾
'''
# 3. 验证read()读取后,光标会留在读取末尾
print('第二次读取')         #输出:第二次读取  
print(file.read())         #输出:   (什么都没有输出)
print('第二次读取结束')     #输出:第二次读取结束

# 4. seek(cookie, whence)   cookie参数:光标位置  whence参数:光标截止的位置  即byte offset
file.seek(0)               #光标默认回到开始的位置
print('第三次读取')         #输出:第三次读取  
print(file.read())         #输出:*********(文件里所有内容)
print('第三次读取结束')     #输出:第三次读取结束

# 5. close()  关闭输入输出流，关闭后将无法读取
file.close()
print('第四次读取')         #输出:第四次读取  
print(file.read())         #输出:报错信息  ValueError: I/O operation on closed file.

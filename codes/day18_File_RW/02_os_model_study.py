#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    os模块：系统模块

    备注:本人Python开发环境：Windows系统,使用VS Code来编写代码.通过Terminal来执行程序
"""
import os

# 1. os.name()   输出字符串指示正在使用的平台。如果是window 则用'nt'表示，对Linux/Unix用户，它是'posix'。
print(os.name)  # 输出:nt

# 2. os.getcwd() 函数得到当前工作目录，即当前Python脚本工作的目录路径。
print(os.getcwd())  # 输出:F:\WorkSpaces\python-basic\codes\day18_File_RW

# 3. os.listdir()  返回指定目录下的所有文件和目录名。无参则默认输出当前工作目录下的文件
print(os.listdir())  # 输出:['01_path_study.py', '02_os_model_study.py']

# 4. os.chdir()   切换到目标路径
os.chdir('C:\\Users\\HBlock\\Desktop')  # 切换到桌面
print(os.getcwd())  # 输出:C:\Users\HBlock\Desktop  发现当前路径已经变了
print(os.listdir())  # 输出:******* (太多,不展示了)

# 5. os.remove()  删除一个文件。默认在当前目录下找文件，找到则删除,找不到则报错。(相对路径下寻找)
# os.remove('sss.txt')   # 输出:FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'sss.txt'
# os.remove('test.txt')

# 6. os.path.split() 查看路径的文件夹部分和文件名部分
'''
    将路径分解为(文件夹,文件名)，返回的是元组类型。
    若路径字符串最后一个字符是\,则只有文件夹部分有值,文件名为空字符串；
    若路径字符串中均无\,则只有文件名部分有值。
    若路径字符串有\，且不在最后，则文件夹和文件名均有值。且返回的文件夹的结果不包含\.
'''
path1 = 'C:/Users/HBlock/Desktop/git命令总结.txt'
result = os.path.split(path1)
print(type(result))  # 输出:<class 'tuple'>
print(result)  # 输出:('C:/Users/HBlock/Desktop', 'git命令总结.txt')

path2 = 'C:/Users/HBlock/Desktop/'
result = os.path.split(path2)
print(result)  # 输出:('C:/Users/HBlock/Desktop', '')

# 7. os.path.exists(path) 文件或文件夹是否存在，返回True 或 False
result = os.path.exists('asdadasd.txt')  # 查看文件是否存在,默认在当前工作目录下找
print(result)  # 输出:False

result = os.path.exists('C:\\Users\\HBlock\\Desktop')  # 查看文件夹是否存在
print(result)  # 输出:True

#!/usr/bin/python 

# -*- coding: utf-8 -*-
"""
    pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。

    python的pickle模块实现了基本的数据序列和反序列化

    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储

    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

    pickle.dump() / pickle.load()

    file文件的write(),必须是写入字符串。pickle.dump()写入的是按Python原数据的格式写入的
"""
import pickle

# 1.存储  .pkl文件
dic = {'1': [1, 3, 4, 5, 24131, 'ad', 3], 2: '12312312', '3': (1, 'ad', 45, 213, 'd')}
path_pkl = 'F:/WorkSpaces/python-basic/program_data/test_pkl.pkl'

# 打开要存储的文件,如果没有则新建一个
pick_w = open(path_pkl, 'wb')  # 以二进制来存储：rb, wb, wrb, ab

print(pick_w)  # 输出:<_io.BufferedWriter name='F:/WorkSpaces/python-basic/program_data/test_pkl.pkl'>
print(type(pick_w))  # 输出:<class '_io.BufferedWriter'>

# 写入数据
pickle.dump(dic, pick_w)

# 关闭文件流
pick_w.close()

# 2. 读取.pkl文件
pick_r = open(path_pkl, 'rb')
dic_data = pickle.load(pick_r)
print(dic_data)

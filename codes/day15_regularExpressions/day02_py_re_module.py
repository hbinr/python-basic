'''
    Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义
    
    推荐博客：Python3 如何优雅地使用正则表达式
            https://www.cnblogs.com/LoveFishC/p/4218366.html
            https://www.cnblogs.com/LoveFishC/p/4218375.html
'''
import re
#注意：\转义的坑
s = 'anc\\sno-2s24'   #Python的字符串
# 对应的正则表达式字符串变成：anc\sno-2s24
#所以在最好用原始字符串来表示正则表达式
str_r = r'anc\\sno-2s24'
print(str_r)          #anc\\sno-2s24


'''
    1、re.findall用法
'''
#练习1：找到str_r里面的所有数字
result  = re.findall(r'\d',str_r)
print(result)         #['2', '2', '4']，返回的是列表，元素类型都为字符串
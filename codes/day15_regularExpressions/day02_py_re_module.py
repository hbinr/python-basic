'''
    Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义
    
    推荐博客：Python3 如何优雅地使用正则表达式
            https://www.cnblogs.com/LoveFishC/p/4218366.html
            https://www.cnblogs.com/LoveFishC/p/4218375.html
'''
import re
#注意：'\'转义的坑
s = 'anc\\sno-2s24'   #Python的字符串
# 对应的正则表达式字符串变成：anc\sno-2s24
#所以在最好用原始字符串来表示正则表达式
str_one = r'anc\\sno-2s24'
print(str_one)          #anc\\sno-2s24


'''
    1、re.findall用法， findall(pattern, string, flags=0)
    入参：pattern为传入正则表达式，string为传入要匹配的字符串，
    flags为匹配的模式(默认为0)，其中re.S使匹配包括换行在内的所有字符。findall()函数是逐行匹配的。
    
'''
#练习1：找到str_r里面的所有数字
result  = re.findall(r'\d',str_one)
print(result)         #['2', '2', '4']，返回的是列表，元素类型都为字符串

'''
    2、数量词  {number}   贪婪与非贪婪
    findall()返回的列表中，每个元素都是单个字符，如果想要返回多个字符(字符集或称为字符串)，通过数量词来
    控制
'''
str_two = 'python 80284 java!,3.2w.32 golang24'

result  = re.findall(r'[a-z]{3}',str_two)
print(result)          #['pyt', 'hon', 'jav']
'''
    [a-z]{3}匹配a-z的字母，个数为3，
'''

#如果只是想返回编程语言？ 3个字符不足以满足需求，以下为具体方法，数量词加了范围
result  = re.findall(r'[a-z]{3,6}',str_two)
print(result)          #['python', 'java', 'golang']
'''
    那么问题来了，既然数量词范围是{3,6}，那匹配到3个字符的结果怎么没有返回呢，比如'pyt','hon'
    但结果却只返回了都是编程语言的结果。
    解析：Python中正则表达式默认是贪婪匹配的。
        正则表达式有贪婪与非贪婪的概念：
        贪婪：匹配尽可能多的字符
        非贪婪：也就是尽可能少匹配.{}后面加? 
'''

'''
    3、切分字符串
    用正则表达式切分字符串比用固定的字符更灵活
'''

#看正常的切分代码：
str_three = 'ab c   d'
result = str_three.split(" ");
print(result)         #['ab', 'c', '', '', 'd']  结果带有两个空格

#调用re模块的split(),返回不带空格的结果
result = re.split(r'\s+',str_three)
print(result)         #['ab', 'c', 'd']

#再来个复杂点的
str_four = 'a,b, c , ,, d'
result = re.split(r'[\s\,]+',str_four)
print(result)         #['a', 'b', 'c', 'd']

'''
    4、分组
    除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
    re.match()
'''
str_five = re.match()
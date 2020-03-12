"""
    Python提供re模块，包含所有正则表达式的功能。
    
    推荐博客：Python3 如何优雅地使用正则表达式
            https://www.cnblogs.com/LoveFishC/p/4218366.html
            https://www.cnblogs.com/LoveFishC/p/4218375.html
"""
import re

# 由于Python的字符串本身也用\转义，格外注意：'\'转义的坑
s = 'anc\\sno-2s24'  # Python的字符串
# 对应的正则表达式字符串变成：anc\sno-2s24
# 所以在最好用原始字符串来表示正则表达式
str_regx = r'anc\\sno-2s24'
print(str_regx)  # anc\\sno-2s24

'''
    1、re.findall用法， findall(pattern, string, flags=0)
    pattern：正则表达式，
    string：要匹配的字符串，
    flags：匹配的模式(默认为0)，findall()函数是逐行匹配的。
    
'''
# 练习1：找到str_r里面的所有数字
result = re.findall('\d', str_regx)
print(result)  # ['2', '2', '4']，返回的是列表，元素类型都为字符串

'''
    2、数量词  {number}   贪婪与非贪婪
    findall()返回的列表中，每个元素都是单个字符，如果想要返回多个字符(字符集或称为字符串)，通过数量词来
    控制
'''
# 练习2：{number}
str_regx = 'python 80284 java!,3.2w.32 golang24'
result = re.findall(r'[a-z]{3}', str_regx)
print(result)  # ['pyt', 'hon', 'jav']
'''
    [a-z]{3}匹配a-z的字母，个数为3，
'''

# 如果只是想返回编程语言？ 3个字符不足以满足需求，以下为具体方法，{m,n}或者{m-n}  表示m到n的范围
result = re.findall(r'[a-z]{3,6}', str_regx)
print(result)  # ['python', 'java', 'golang']
'''
    那么问题来了，既然数量词范围是{3,6}，那匹配到3个字符的结果怎么没有返回呢，比如'pyt','hon'
    但结果却只返回了都是编程语言的结果。
    解析：Python中正则表达式默认是贪婪匹配的。
        正则表达式有贪婪与非贪婪的概念：
        贪婪：匹配尽可能多的字符
        非贪婪：也就是尽可能少匹配  {}后面加?即可表示非贪婪模式 
'''

# 练习3：  * 匹配0次或者多次，r'python*'这个表达式的含义是'*'前面的n可以出现0次或者多次
str_regx = 'pytho1python2pyt23pythonnnnnn222'
result = re.findall(r'python*', str_regx)  # ['pytho', 'python', 'pythonnnnnn']
print(result)

# 练习4：  + 匹配1次或者多次，r'python*'这个表达式的含义是'+'前面的n可以出现1次或者多次
str_regx = 'pytho1python2pyt23pythonnnnnn222'
result = re.findall(r'python+', str_regx)  # ['python', 'pythonnnnnn']
print(result)

# 练习5：  ? 匹配0次或者1次，r'python?'这个表达式的含义是'?'前面的n可以出现0次或者1次，常用于字符串去重
# 注意：此处的'?'和'{}?'表示的不是同一个概念，后者是表示非贪婪模式
str_regx = 'pytho1python2pyt23pythonnnnnn222'
result = re.findall(r'python?', str_regx)  # ['pytho', 'python', 'python']
print(result)

str_regx = 'one1 hellow! '
print('练习6-------------')
print(re.match(r'.?1', str_regx))  # None  因为'.?e' 以e结尾，e前面有0个或一个字符(用?表示0个或1个字符)
print(re.match(r'.?n', str_regx))  # <re.Match object; span=(0, 2), match='on'>


'''
    3、切分字符串
    用正则表达式切分字符串比split()更灵活
'''

# 看正常的切分代码：
str_regx = 'ab c   d'
result = str_regx.split(" ");
print(result)  # ['ab', 'c', '', '', 'd']  结果带有两个空格

# 调用re模块的split(),返回不带空格的结果
result = re.split(r'\s+', str_regx)
print(result)  # ['ab', 'c', 'd']

# 再来个复杂点的
str_regx = 'a,b, c , ,, d'
result = re.split(r'[\s\,]+', str_regx)
print(result)  # ['a', 'b', 'c', 'd']

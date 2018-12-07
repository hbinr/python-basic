'''
    re模块相关模式参数
    re.I 忽略大小写
    re.S 匹配包括换行在内的所有字符

'''
import re

'''
    特别注意：原始字符串，对正则表达式的匹配影响非常大，
'''
#原始字符串
str_regx = r'PythonGolang\n93u49s93ndfronger'
print(str_regx)
#练习1：忽略大小写，返回Python
result = re.findall(r'python', str_regx, re.I)
print(result)        #['Python']

#练习2： 输出包括换行符\n在内的字符串，返回Python
result = re.findall(r'Golang.{1}', str_regx, re.S)
print(result)        #['Golang\\']  why??

#不是原始字符串
str_regx = 'PythonGolang\n93u49s93ndfronger'
print(str_regx)     #PythonGolang   字符串换行显示了
                    #93u49s93ndfronger
result = re.findall(r'python', str_regx, re.I)
print(result)        #['Python']

result = re.findall(r'Golang.{1}', str_regx, re.S)
print(result)        #['Golang\n']   输出了\n

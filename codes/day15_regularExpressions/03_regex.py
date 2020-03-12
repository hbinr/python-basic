"""
    分组  加()来表示一组
    https://www.cnblogs.com/cute/p/9186208.html
    1、用于匹配括号内的任何正则表达式,并且指明组的开始和结束位置;可以在执行匹配之后检索组中的内容,
    并且可以在字符串中使用\number来进行进一步的匹配。
    当需要匹配字符’(‘或者’)’时,可以使用(和) ,或者[(]和[)]来实现。
    2、()的作用
          1). 捕获()中正则表达式的内容以备进一步利用处理，可以通过在左括号后面跟随?:来关闭这个括号的捕获功能
　　　　　　2). 将正则表达式的一部分内容进行组合，以便使用量词或者|

    匹配模式参数
    3、match()
    re.match(pattern, string, flags=0) → 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
    pattern：匹配的正则表达式
    string：要匹配的字符串。
    flags：标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
"""
import re

'''
    1、组的练习
    目的：打印出连续4个python的字符串
'''
str_regx = 'PythonPythonPythonPythonPythonPythonPython'

result1 = re.findall(r'(Python){4}', str_regx)  # (Python){4}是表示 PythonPythonPythonPython吗？
print(result1)  # ['Python']
# 测试下这个想法，将正则表达式改为PythonPythonPythonPython，发现结果是：['PythonPythonPythonPython']，
result2 = re.findall(r'PythonPythonPythonPython', str_regx)
print(result2)  # ['PythonPythonPythonPython']
''' 
    好奇怪，那试试使用match()，运行后发现(Python){4}的确是表示PythonPythonPythonPython，
    为什么result1会是 ['Python'] 这种结果？？
    TODO
    
'''
result3 = re.match('(Python){4}', str_regx)
print(result3.group())  # PythonPythonPythonPython

'''
    2、match()函数练习
'''
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

str_regx1 = 'Hello World!'
matchob = re.match(r'!$', str_regx1)  # !$ 匹配以!结尾的字符串
print(matchob)  # None  由于match是从开头位置(此处为H)开始匹配的，所以无法匹配
print(re.match(r'.*!$', str_regx1))  # <re.Match object; span=(0, 12), match='Hello World!'>
# 匹配!结尾并设置!之前为任意个字符 匹配成功

'''
    https://blog.csdn.net/djskl/article/details/44357389
    
    3、group()
    group()：母串中与模式pattern匹配的子串；
    group(0)：结果与group()一样；
    groups()：所有group组成的一个元组，group(1)是与patttern中第一个group匹配成功的子串，
    group(2)是第二个，依次类推，如果index超了边界，抛出IndexError；
'''

'''
    4、span()
    通过span()方法用于以元祖形式返回匹配的起始位置和结束位置
    span() 返回一个元组包含匹配 (开始,结束) 的位置
    start() 返回匹配开始的位置
    end() 返回匹配结束的位置
'''

# span()练习
str_regx2 = '今天星期一'
matchob1 = re.match(r'今天.', str_regx2)
print(type(matchob1))  # <class 're.Match'>
print(matchob1.span())  # (0, 3)
print(matchob1.group())  # 今天星

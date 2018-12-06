'''
    分组  加()来表示一组
    用于匹配括号内的任何正则表达式,并且指明组的开始和结束位置;可以在执行匹配之后检索组中的内容,
    并且可以在字符串中使用\number来进行进一步的匹配。
    当需要匹配字符’(‘或者’)’时,可以使用(和) ,或者[(]和[)]来实现。

    匹配模式参数

'''
import  re
str_regx = 'PythonPythonPythonPythonPythonPythonPython'
#打印出连续三个python的字符串
result = re.findall(r'(Python){2}',str_regx)
print(result)

# import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("No match!!")
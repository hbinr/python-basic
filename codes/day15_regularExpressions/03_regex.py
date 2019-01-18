'''
    分组  加()来表示一组
    https://www.cnblogs.com/cute/p/9186208.html
    1、用于匹配括号内的任何正则表达式,并且指明组的开始和结束位置;可以在执行匹配之后检索组中的内容,
    并且可以在字符串中使用\number来进行进一步的匹配。
    当需要匹配字符’(‘或者’)’时,可以使用(和) ,或者[(]和[)]来实现。
    2、()的作用
          1). 捕获()中正则表达式的内容以备进一步利用处理，可以通过在左括号后面跟随?:来关闭这个括号的捕获功能
　　　　　　2). 将正则表达式的一部分内容进行组合，以便使用量词或者|

    匹配模式参数

'''
import  re

'''
    1、组的练习
    目的：打印出连续4个python的字符串
'''
str_regx = 'PythonPythonPythonPythonPythonPythonPython'

result1 = re.findall(r'(Python){4}',str_regx)     #(Python){4}是表示 PythonPythonPythonPython吗？
print(result1)   #['Python']
#测试下这个想法，将正则表达式改为PythonPythonPythonPython，发现结果是：['PythonPythonPythonPython']，
result2 = re.findall(r'PythonPythonPythonPython',str_regx)
print(result2)     #['PythonPythonPythonPython']
''' 
    好奇怪，那试试使用match()，运行后发现(Python){4}的确是表示PythonPythonPythonPython，
    为什么result1会是 ['Python'] 这种结果？？
    TODO
    
'''
result3 = re.match('(Python){4}',str_regx)
print(result3.group())    #PythonPythonPythonPython

'''
    match()函数练习
'''
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("No match!!")


'''
    https://blog.csdn.net/djskl/article/details/44357389
    2、match()函数从首字母开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，
    失败则返回None，若要完全匹配，pattern要以$结尾。
    group()：母串中与模式pattern匹配的子串；
    group(0)：结果与group()一样；
    groups()：所有group组成的一个元组，group(1)是与patttern中第一个group匹配成功的子串，
    group(2)是第二个，依次类推，如果index超了边界，抛出IndexError；
'''
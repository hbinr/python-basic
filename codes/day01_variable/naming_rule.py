#1、变量命名规则: 由字符、数字、下划线组合，且数字不能作为命名开头
# 1age = 20;  #语法错误 SyntaxError: invalid syntax
name = "Tom"
_sex = 'male'
_age18 = 18
print(name) #Tom  字符串
print(_sex) #male 字符串
print(_age18) #18 int型

'''
    在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
'''


#2、不能以python中的关键字来命名，这些关键字又称保留关键字，如:where and if else  import for def等
#在python_is_keyword程序中打印了python中所有的保留关键字
#type不是保留关键字，尽管经常用type()来查看类型，但是不能用来作为变量名的。类似的还有print等
print(type("hello world"))  #<class 'str'>
type = 1
type("hello world") #TypeError: 'int' object is not callable  ---类型错误:“int”对象不可调用
#type已经被赋值1了，然后再去调用type()不可行的，上面这段代码相当于 1("hello world")

#3、变量名区分大小写
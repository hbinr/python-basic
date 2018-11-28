'''
    一、什么是变量作用域呢？
    在维基上给出的定义是“The scope of a variable describes where in a program's text the variable may be used, 
    while the extent (or lifetime) describes when in a program's execution a variable has a (meaningful) value.
    ”简而言之就是两点，在何处可以使用变量以及标识符绑定的值生存多久。
    二、LEGB原则：Python的作用域规则最出名的就是LEGB，这四个字母的含义代表着Python的对于变量的查找顺序：
    locals -> enclosing -> globals -> builtins。
    

    参考：https://www.cnblogs.com/fireporsche/p/7813961.html
'''

'''
    1、Python变量的作用域由变量所在源代码中的位置决定。只有当变量在Module(模块)、Class(类)、def(函数)中定义的时候，
    才会有作用域的概念，并不是所有的语句块都会产生作用域
'''
result = 50
def add(x,y):
    result = x + y;
    print(result)

add(1,2)         #3  打印的是def函数中的变量值
print(result)    #50  而不是3，虽然result名字相同，但是作用域不同。def函数中的变量result在其内部可以访问，其他地方无法访问
                 #测试，当注释掉result=50时，结果报错：NameError: name 'result' is not defined

'''
    2、在作用域中定义的变量，一般只在作用域中有效。 需要注意的是：
    在if-elif-else、for-else、while、try-except\try-finally等关键字的语句块中并不会产成作用域。
    看下面的代码：
'''
if True:
    variable = 100
    print (variable)
print ("******")
print (variable)
#结果为：  虽然是在if语句中定义的variable变量，但是在if语句外部仍然能够使用
# 100
# ******
# 100

'''
    3、作用域的类型
'''
'''
    在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号 ':'
    
    然后，在缩进块中编写函数体，函数的返回值用return语句返回。
    
    值得注意的是，返回值不用显式声明，且返回类型可以是任意变量(动态语言特性)
    
    函数执行完毕也没有return语句时，自动return None。
    
    函数可以同时返回多个值，但其实就是一个tuple。
'''
import sys
sys.setrecursionlimit(10000)  #设置递归执行的最大次数为10000，但是在实际执行时，系统会弹窗"Python已停止工作"
#练习1：
def add(x,y):
    return x + y or "计算错误！"

# def print(code):
#     print(code)

add(1,2)
# print("python")  #[Previous line repeated 995 more times] 递归执行print()995次后抛出错误
                   #原因是自定义的方法名和python内置函数print重名了，导致递归调用

#修改后
def print_code(code):  #该函数未定义返回值，默认返回None
    print(code)

a = add(1,2)
b = print_code("python")       #python   执行print_code()
print(a,b)                     #3   None(print_code未定义返回值)

#练习2：空函数   pass占位符
'''
    之所以要加这个练习，是pass占位符在实际开发中经常用到。
    pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
    就可以先放一个pass，让代码能运行起来。
    去掉pass，程序则会报错
'''
def emptyFunc():
    pass

#练习3：返回多个结果

def multiplication(arg1,arg2):
    resutlOne = arg1 * 10
    resutlTwo = arg2 * 20
    return resutlOne, resutlTwo

result  = multiplication(10,10)
print('multiplication的返回值为：',result)   #(100, 200)  返回值为元组类型

'''
如何利用函数返回值？ 既然返回的是一个元组，在取每个返回值时，都要result(序号)来获取相应的值？
    实际在开发中不推荐这种写法，如果过段时间后，大量的result[0],result[1],result[2]...  自己都不记得每个序号代表什么含义了
推荐以下方式： 最好返回值在命名时体现其实际意义
'''
resultOne, resultTwo = multiplication(10,20)
print(resultOne,resultOne)

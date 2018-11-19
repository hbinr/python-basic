'''
    内置函数之dir(),返回指定对象或模块obj的成员列表，如果不带参数则返回当前作用域的所有标识符
    如果想查看某块下有什么变量或者函数。可以使用dir()
'''
import  sys

infos = dir(sys)
print(infos)          #输出一个列表，包含了sys模块下的所有成员
print(sys.__name__)   #sys
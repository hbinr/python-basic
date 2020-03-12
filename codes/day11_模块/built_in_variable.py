"""
    主要记录Python的内置变量
    python模块，除了有自定义变量，模块本身还有一些内置变量
    内置函数dir()返回指定对象或模块obj的成员列表，如果不带参数则返回当前作用域的所有标识符
"""

'''
    这是第二段文档注释
'''
import day11_模块.cycle2

temp = 1
infos = dir()  # 打印出当前模块所有的变量
print(
    infos)  # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'temp']

# 可以看到，除了temp显式变量，还打印出了很多内置变量。重点学习下:__doc__，__file__，__name__，__package__ 这四个内置变量

# 1、__doc__   文档注释
print("builr_in_variable模块的__doc__值为：" + __doc__)  # 文档注释 ，只打印当前模块第一个文档注释   上面的"这是第二段文档注释"并没有打印

# 2、__file__       #系统内文件的完整路径(当前是window10系统)
print("builr_in_variable模块的__file__值为：" + __file__)  # F:/WorkSpaces/python-basic/codes/day11_模块/built_in_variable.py
'''
注意：__file__的值和python执行程序命令有关，它所表示的是执行程序时，打印在执行命令下，文件所在的位置
实践:
第一步:cd codes      #进入codes目录
第二步:python day11_模块\cycle2.py      #执行该程序
查看结果：
cycle2模块的__file__值为： day11_模块\cycle2.py
可以看到，__file__的值不再是刚才那么一大串了

'''

# 3、__name__  命名空间+模块名称，没有命名空间就只显示模块名称
print("builr_in_variable模块的__name__值为：" + __name__)  # __main__，当前运行的程序(入口文件)，会执行__main__方法

# 4、__package__   python包名
print("builr_in_variable模块的__package__值为：" + (__package__ or '当前模块不属于任何包'))  # None 当前模块不属于任何包 注意()的使用

'''
#注意区分cycle2模块中的输出和本模块的输出做比较
cycle2模块的输出内容：
This is a cycle2 module
cycle2模块的__doc__值为： None
cycle2模块的__file__值为： F:\WorkSpaces\python-basic\codes\day11_模块\cycle2.py
cycle2模块的__name__值为： day11_模块.cycle2
cycle2模块的__package__值为： day11_模块

输出的结果有差异，原因是：当前模块运行后，被认作为是入口文件，在python中，入口文件和普通模块的内置变量是有区别的 
区别：
1、__name__值：入口文件为：__main__；而普通模块则是其命名空间+模块名称
2、__package__值：入口文件是没有包的，结果为：None；而普通模块则是其包名。
3、普通模块是必须有包，而入口文件则没有这个强制要求
'''

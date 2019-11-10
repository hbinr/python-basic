import  package1.m1

#使用绝对导入的方式导入m4模块
import  package1.package4.m4

#使用相对导入的方式导入m4模块
# import .package4.m4   无法导入，IDEA直接报错，语法错误
# from .package1.package4.m4 import temp4    #运行错误  找不到模块名

#错误内容： ModuleNotFoundError: No module named '__main__.package1'; '__main__' is not a package
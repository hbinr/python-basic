"""
    本模块主要记录包和模块常见的错误

"""

# 1、循环导入，类似Java使用maven管理依赖时，循环导入依赖。无论时直接导入还是间接导入，都有可能出现循环导入的情况。

# 练习：cycle1导入common_mistakes模块，而common_mistakes同时也导入了cycle1模块
#
# from day11_模块.cycle1 import  cy1
# common = "common_mistakse"
# print("This is common_mistakse module")
# print("I want to print cycle1's variable", cy1)

'''
报错截图详见: pictures/循环导入模块案列.png。
解析:运行common_mistakse.py模块，在程序行：print("I want to cycle1's variable",cy.cy1)打印cy.cy1报错，然后堆栈信息
追朔到cycle1.py模块，而改模块的代码第一行执行了import day11_模块.common_mistakes as common，
所以又要去运行一次common_mistakse.py模块，所以还会再次遇到上述问题，就造成循环导入，程序报错了
'''

# 2、循环导入，另一种导入方式报错
import day11_模块.cycle1 as cy

print("I want to print cycle1's variable", cy.cy1)
'''
    报错：AttributeError: module 'day11_模块.cycle1' has no attribute 'cy1'
    解析：运行common_mistakse.py模块，import day11_模块.cycle1 as cy时，会去执行cycle1模块，而cycle1模块又执行了
    import day11_模块.common_mistakes as common  代码，因此造成了循环导入错误，而Python是解释性语言，所以cycle1模块
    cy1并没有被解释到，因此才会报：has no attribute 'cy1'
    
    为什么两种导入方式，报错原因不一样：
    import一般是导入模块，而from  import通常是导入变量，模块和变量还是有很大区别的
'''
# 3、包和模块是不会重复导入的

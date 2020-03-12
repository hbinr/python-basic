"""
    在大型软件开发时，不可能把所有代码放在通过一个文件下，也不可能是单一的几个文件就能囊括整个项目需要的代码。在实际开发中，
根据功能的不同，会将代码分为不同的模块来进行开发和维护，每个模块间可能会有调用联系，比如A模块需要调用B模块返回的结果来
进行相应的业务处理。
    对于大型系统，可以用包来管理多个模块，包是Python用来组织命名空间的重要方式，可以看作包是含大量Python程序模块的文件夹。
在包的每个子文件夹中都必须包含一个__init__.py文件，该文件可以是一个空文件夹，仅用于表示当前文件夹是一个python包。
    __init__.py文件的主要用途是设置__all__变量以及执行初始化包所需的代码，其中__all__变量定义的对象可以在使用
"from xxx import  *"时被正确导入。__all__通常时一个列表，必须是序列,python通过序号来找到相应的模块、函数或变量。不能是集合。
    在导入包的时候，python就会自动__init__.py文件，进行初始化

    总结 __init__作用
    1. 初始化 __all__内置变量  前提时导包时写有import *
    2. 初始化项目需要的类库，批量导入
"""
# 练习1:导入test包下的test1和test2模块
# from test import *       # 只会引入test模块的内置变量__all__，test模块的__init__.py会执行
# This is a test1 module

# 练习2:打印当前时间
import test  # 不会引入test模块的内置变量__all__，但test模块的__init__.py会执行

curr_date = test.datetime.datetime.now()
print("当前时间为:", curr_date)  # 当前时间为: 2018-11-19 15:34:26.928746 调用时要加上相对路径 'test.datetime'

# 验证内置变量是否被引入
print(test.test1.t1)  # AttributeError: module 'test' has no attribute 'test1'

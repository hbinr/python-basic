"""
    成员方法:
    首先明确，在面向对象程序设计中，函数和方法是有本质区别的：
        方法一般指与特定实例绑定的函数，通过对象调用方法，对象本身将作为第一个参数自动传递过去，而普通函数并不具备这
    个特点。例如：内置函数sorter()必须要指明排序的对象，而列表对象的sort()方法则不需要，默认是对当前列表排序。list.sort()

    Python中的成员方法大致可以分为：公有方法、私有方法、静态方法、类方法和抽象方法
    公有方法，私有方法，抽象方法一般是指属于对象的实例方法。私有方法的名字以两个或多个下划线开始，而抽象方法一般定义在
    抽象类中并且要求派生类必须重新实现。

"""


class Root:
    sum = 1
    __total = 0  # 类私有变量

    def __init__(self, v):
        self.__value = v  # 对象私有变量
        Root.__total += 1  # 每次实例化对象， __total都加1，表示实例化了几个对象

    def show(self):  # 普通实例方法，公有。
        print('self.__value：', self.__value)
        print('Root.__total：', Root.__total)

    @classmethod
    def test_cls_method(cls):
        cls.__total += 1  # 可以访问类变量
        print('我是一个类方法，_total为：', cls.__total)

    @staticmethod
    def test_static_method():
        print('我是一个静态方法', Root.sum)  # 可以访问类变量


'''
    一、公有方法 
    公有方法通过对象名直接调用
'''

# 实例化对象
root1 = Root(18)

# 通过类名直接调用普通实例方法
# Root.show()    #TypeError: show() missing 1 required positional argument: 'self'  报错
'''
    报错的原因：在外部通过类名调用属于对象(show方法声明了当前对象self)的公有方法，需要显式为该方法的self参数传递一个
    对象名，用来明确指定访问哪个对象的成员
'''

# 正确调用
Root.show(root1)  # self.__value： 18
# Root.__total： 1

'''
    二、私有方法
    私有方法不能通过对象名直接调用，只能在其他实例方法中通过前缀self进行调用或在外部通过特殊的形式来调用
'''

'''
    三、类方法  关联的是类本身
    1)参数为cls  注意，规范是cls,可以写为class，self都可以，只是个命名。因此不要看到一个方法的参数列表里有self就认为是实例方法
    2)有装饰器@classmethod  这个是必须的
    可以调用类变量，不可以调用实例变量
'''
# 类名调用
Root.test_cls_method()  # 我是一个类方法，_total为： 2

# 对象名调用  最好使用类名调用，规范
root1.test_cls_method()  # 我是一个类方法，_total为： 3

'''
    三、静态方法
    有装饰器@staticmethod  这个是必须的
    无参数限制，和实例方法(self)、类方法(cls)不同
    可以调用类变量，不可以调用实例变量
'''
# 类名调用
Root.test_static_method()  # 我是一个静态方法 1

# 对象名调用  最好使用类名调用，规范
root1.test_static_method()  # 我是一个静态方法 1

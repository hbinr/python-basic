'''
    成员方法:
    首先明确，在面向对象程序设计中，函数和方法是有本质区别的：
        方法一般指与特定实例绑定的函数，通过对象调用方法，对象本身将作为第一个参数自动传递过去，而普通函数并不具备这
    个特点。例如：内置函数sorter()必须要指明排序的对象，而列表对象的sort()方法则不需要，默认是对当前列表排序。list.sort()

    Python中的成员方法大致可以分为：公有方法、私有方法、静态方法、类方法和抽象方法
    公有方法，私有方法，抽象方法一般是指属于对象的实例方法。私有方法的名字以两个或多个下划线开始，而抽象方法一般定义在
    抽象类中并且要求派生类必须重新实现，。

'''
class Root:
    __total = 0      #类私有变量
    def __init__(self, v):
        self.__value = v      #对象私有变量
        Root.__total += 1     #每次实例化对象， __total都加1，表示实例化了几个对象

    def show(self):           #普通实例方法，公有。一般以self
        print('self.__value：',self.__value)
        print('Root.__total：',Root.__total)

'''
    公有方法通过对象名直接调用，私有方法不能通过对象名直接调用，只能在其他实例方法中通过前缀self进行调用或在外部通过特殊
    的形式来调用
'''

#实例化对象
root1 = Root(18)

#通过类名直接调用普通实例方法
Root.show()    #TypeError: show() missing 1 required positional argument: 'self'  报错
'''
    报错的原因：在外部通过类名调用属于对象(show方法声明了当前对象self)的公有方法，需要显式为该方法的self参数传递一个
    对象名，用来明确指定访问哪个对象的成员
'''

#正确调用
Root.show(root1)        #self.__value： 18
                        #Root.__total： 1
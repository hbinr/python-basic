"""
    构造函数：
    __init__()，用来为数据成员设置初始值或进行其他必要的初始化工作，在实例化对象时自动被调用和执行。如果用户没有设计
    构造函数，Python会提供一个默认的构造函数用来进行必要的初始化工作。

    析构函数：
    __del__()，一般用来释放对象占用的资源，在Python删除对象和回收对象空间时被自动调用和执行，同样的，如果用户没有设计
    析构函数，Python也会提供一个默认的
"""


class Student():

    def __init__(self):
        print("进入构造函数")
        # return 'student1实例'     # 如果在构造函数增加返回值，在实例化对象时，会报错
        # TypeError: __init__() should return None, not 'str'

    def my_print(self):
        print("This is my_print function")


# 实例化一个student1，会默认执行构造函数
student1 = Student()  # 进入构造函数   根据输出结果，可见在实例化对象时，会默认执行构造函数

# 那如果显式的去调用构造函数，返回值是什么呢？
a = student1.__init__()
print(a)  # None   可见构造函数是没有返回值的，那可以不可以重写默认构造函数，返回一个结果呢？
'''
    在__init__增加了返回值后，发现程序运行报错，在python中，构造函数是强制返回None的，不能再定义其他的返回值
    TypeError: __init__() should return None, not 'str'
'''


class Teacher():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('%s:%s' % (self.name, self.age))  # %s 格式化表示为字符串


# 通过构造函数，Teacher类在实例化对象，传入不同的参数就会实例化不同的对象
teacher = Teacher('Tom', 20)  # Tom:20
teacher2 = Teacher('Tony', 22)  # Tony:22

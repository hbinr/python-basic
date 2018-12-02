'''
    OO_7  super()
    super() 函数是用于调用父类(超类)的一个方法。

    super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，
    会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

    MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
    
'''

class Animal():
    def __init__(self, name, age, gendor):
        self.name = name
        self.age = age
        self.__gendor = gendor

    def run(self):
        print("动物具有跑的能力")

    def eat(self):
        print("动物具有吃的能力")

#定义Dog类，并继承Animal类
class Dog(Animal):
    def __init__(self, species, name, age, gendor):   #增加一个种类的属性，父类的属性也要加入
        #调用父类的构造函数
        Animal.__init__(name, age, gendor)
        self.species = species

    def eat(self):
        print("狗喜欢吃肉")

#实例化dog对象
dog = Dog('阿黄', 2, '公','牧羊犬')

'''
    运行报错：
    TypeError: __init__() missing 1 required positional argument: 'gendor'
    位置参数丢失了一个参数'gendor'

    在学习python时，要对比和静态语言的不同，按照静态语言的逻辑来学习会有很多坑，要想写出Pythonic的代码，
    就要打好基础，Python入门容易，但是精通却比较难
'''

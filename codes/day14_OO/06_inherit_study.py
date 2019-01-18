'''
    OO_6  继承
    刚开始在学习类的时候，简单在定义了提了一下继承，但是一直没有深入学习和实践。今天主要记录继承：
    在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
    而被继承的class称为基类、父类或超类（Base class、Super class）。
    
    继承的作用是
    1、子类获得了父类的全部功能，当然如果子类想实现自己的方法也可以自定义一个实例方法，甚至如果不满意父类已有的方法，
    子类也可以根据自己的需要来重写父类的方法
    
    2、减少了重复代码，提升效率
    
    3、在实际开发中，子类和父类可能存在完全相同的方法，子类就会覆盖父类的方法，代码运行时，总是会调用子类的方法。这样，
    继承的另一个好处派上用场了：多态
    
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
    def eat(self):
        print("狗喜欢吃肉")

#实例化dog对象，注意，要传入父类构造函数中的参数，否则会报错
# dog = Dog() #TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'gendor'
dog = Dog('阿黄', 2, '公')

#访问父类中的公有变量
print("Animal类的实例变量name:",dog.name)    #Animal类的实例变量name: 阿黄

#访问父类中的私有变量
print("Animal类的实例变量__gendor:",dog.__gendor)
#AttributeError: 'Dog' object has no attribute '__gendor'
#会报错  ，因为私有变量只有本类可以访问，子类都不允许

#调用父类run()，输出结果为父类run()的内容
dog.run()      #动物拥有跑的能力

#调用eat()，输出结果为子类重写eat()的内容
dog.eat()      #狗喜欢吃肉     子类就会覆盖父类的方法

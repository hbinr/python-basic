'''
    OO_6  继承
    刚开始在学习类的时候，简单在定义里提了一下继承，但是一直没有深入学习和实践。今天主要记录继承：
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


'''
    1、定义子类，并继承Animal类
'''


class Dog(Animal):
    def eat(self):
        print("狗喜欢吃肉")


class Cat(Animal):
    def eat(self):
        print("猫喜欢吃鱼")


# 实例化dog对象，注意，要传入父类构造函数中的参数，否则会报错
# dog = Dog() #TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'gendor'
dog = Dog('阿黄', 2, '公')

'''
    2、操作对象的属性
'''
# 访问父类中的公有变量
print("Animal类的实例变量name:", dog.name)  # Animal类的实例变量name: 阿黄

# 访问父类中的私有变量
# print("Animal类的实例变量__gendor:",dog.__gendor)
# AttributeError: 'Dog' object has no attribute '__gendor'
# 会报错  ，因为私有变量只有本类可以访问，子类都不允许

# 调用父类run()，输出结果为父类run()的内容
dog.run()  # 动物拥有跑的能力

# 调用eat()，输出结果为子类重写eat()的内容
dog.eat()  # 狗喜欢吃肉     子类就会覆盖父类的方法,在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。

'''
    3、多态的使用
    在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
'''
# 多态1：如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类

if isinstance(dog, Animal):
    print("Dog的数据类型是Animal")

print(isinstance(dog, Animal))       # True
# 多态2：开闭原则
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，调用方只管调用，不管细节
# 对扩展开放：允许新增Animal子类；
#
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


def eat_polymorphic(Animal):
    Animal.eat()


eat_polymorphic(dog)  # 狗喜欢吃肉
cat = Cat('阿猫', 2, '公')
eat_polymorphic(cat)  # 猫喜欢吃鱼

'''
    4、静态语言VS动态语言
'''
'''
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用eat()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个eat()方法就可以了：
'''


class Timer(object):
    def eat(self):
        print("Start eating.....")


eat_polymorphic(Timer())  # Start eating..... 可以看到，Timer并没有继承Animal类，但是eat_polymorphic()却可以执行

'''
    这就是动态语言的“鸭子类型”,“file-like object“。
    它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
'''

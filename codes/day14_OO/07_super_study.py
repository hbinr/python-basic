'''
    super() 函数是用于调用父类(超类)的一个方法。

    super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
    但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

    MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
    
'''

class Animal():
    def __init__(self, name, age, gendor):
        self.__name = name
        self.__age = age
        self.gendor = gendor

    def run(self):
        print("动物具有跑的能力")

    def eat(self):
        print("动物具有吃的能力")

#定义Dog类，并继承Animal类
class Dog(Animal):
    def __init__(self, species, name, age, gendor):   #增加一个种类的属性，父类的属性也要加入
        self.species = species
        #调用父类的构造函数
        Animal.__init__(self, name, age, gendor)

    def eat(self):
        print("狗喜欢吃肉")

#实例化dog对象
dog = Dog('牧羊犬','阿黄', 2, '公')
# print('Dog\'s name is',dog.name)

print('Dog\'s name is',dog.gendor)
'''
        运行报错：AttributeError: 'Dog' object has no attribute 'name'
    在实例化对象时不是已经初始化name为'阿黄'了吗？为什么报没有name属性错误。
'''
print(dog.__dict__)    #{'species': '牧羊犬', '_Animal__name': '阿黄', '_Animal__age': 2, 'gendor': '公'}
'''
    打印dog对象的变量后，发现name属性是属于Animal父类的，且是私有的，所以子类无法访问
    
    另外在实例化dog对象时，dog的构造函数调用父类的构造函数，即Animal.__init__(self, name, age, gendor)
    这种调用方式是错误的，应该是 对象名.__init__()，而不是用类名来调用。
    因为类似抽象的，对象是具体的，本身构造函数就是一个特殊的实例方法(应该对象调用)，
    所以用类名去调用是错误的，但是Python并没有作限制。
    
    然后回过头来再想一想，在Dog类里的构造函数里去显式的调用父类的构造函数合适吗？或者说，写法是不是本身就有问题？
    
    其实，Animal.__init__(self, name, age, gendor) 本质上就是类名.方法，就是普通的调用方法方式，所有参数都要显式传递，
    包括self，而Python在实例化对象时调用构造函数并不是这样调用的。因此上述写法本身就存在问题。
    
    值得注意的是：对象在调用实例方法时不需要传递self参数，区别与普通的调用方法方式。因为self表示的含义就是当前对象，
    对象在调用实例方法时，Python自动将self参数传递了。
    
    在大多数静态于语言里，用类名去调用普通方法会报错，比如Java(静态方法可以)  但Python却并没有这个限制
    Python的原则就是没有任何机制阻止你干坏事，一切全靠自觉。
    在学习python时，要对比和静态语言的不同，按照静态语言的逻辑来学习会有很多坑，要想写出Pythonic的代码，
    就要打好基础，Python入门容易，但是精通却比较难
'''

'''
    写了这么多，super()真正的用法还未涉及，其实是抛砖引玉，接下来记录super的用法。
    试想一下：Student类不想继承Human类，要换一个其他，那么凡是调用 Animal.__init__(self, name, age, gendor)的地方，
    类名也得改，如果Student类里有多处都是类似的写法呢，那不是得全部改？这件事想想就觉得不太合理，而且也明显违反了开闭原则，
    对外扩展要开放，但是自身的修改时封闭的，不轻易去改动原有的逻辑。
    因此，super()派上用场了  语法： super().父类属性
'''
#重新定义Cat类，并继承Animal类
class Cat(Animal):
    def __init__(self, species, name, age, gendor):
        self.species = species
        #调用父类的构造函数
        super().__init__(name, age, gendor)

    def eat(self):
        super().eat()       #super调用父类的方法

        # print("猫喜欢吃鱼")

cat = Cat('花猫','阿花', 2, '母')
cat.eat()          #动物具有吃的能力   输出了父类的内容

'''
    Python中有多重继承的用法：
    
    https://www.cnblogs.com/xinghuaikang/p/8481712.html
'''
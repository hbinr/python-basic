'''
    类变量和实例变量
    类变量就是属于类的变量，是该类所有对象共享的，不属于任何一个对象。在定义类时，类变量一般不会定义在任何一个成员方法中。
    类变量可以通过类名或对象名访问，

    实例变量就是属于对象的变量，属于对象的变量一般在构造函数__init__()中定义，当然也可以在其他成员方法中定义。在定义和
    在实例方法中访问数据成员时以self作为前缀，同一个类的不用对象的数据成员之前互不影响。
    实例变量只能通过对象名访问。

'''
class Student():
    name = 'class\'s variable'     #类变量
    age = 0       #类变量
    def __init__(self, name, age):
        self.name = name     #实例变量
        self.age = age       #实例变量

    def  print_info(self, name, age):
        self.name = name     #实例变量
        self.age = age       #实例变量
        print('%s : %s' %(self.name, self.age))

    def test_self(self, name):
        name = name     #实例变量
        print('test_self()中的实例变量：',name)

student1 = Student('茸儿',20)

#访问类变量
print(Student.name)               #class's variable  通过类名访问
print(student1.__class__.name)    #class's variable 间接通过类名来访问
#访问实例变量
print(student1.name)              #茸儿
print(student1.age)               #20

#访问实例方法
student1.print_info('茸儿',20)    #茸儿 : 20

'''
    如果在定义实例变量时没有加self前缀，再次执行print(student1.name) 会是什么结果呢？
'''

class Teacher():
    name = '常老师'
    def __init__(self, name):
        name = name

#实例化一个名叫'王老师'的对象
teacher1 = Teacher("王老师")

#访问刚刚定义teacher1对象的name，即想访问实例变量
print(teacher1.name)        #常老师
'''
    结果并不是我们想象中的王老师，而是常老师(类变量)
'''
#验证teacher1对象里是否有实例变量name    __dict__，表示当前对象所有的变量
print(teacher1.__dict__)    #{}  结果是一个空字典，即teacher1对象里没有任何变量

'''
    既然teacher1对象里没有任何变量，直接打印一个None才是正常的逻辑，但是结果却是常老师。
    这儿需要掌握的知识点是类与变量的查找顺序：
    首先在对象的实例变量查找是否存在name变量，如果没有就继续去类变量查找，找到则打印结果，没有就去父类寻找，如果父类还没有
    则输出错误：AttributeError: 'Teacher' object has no attribute 'name'
    
'''

#类的所有变量__dict__
print(Teacher.__dict__)

'''
结果为：
{'__module__': '__main__', 'name': '常老师', '__init__': <function Teacher.__init__ at 0x000001D75F15D9D8>, 
'__dict__': <attribute '__dict__' of 'Teacher' objects>, '__weakref__': <attribute '__weakref__' of 'Teacher' objects>,
 '__doc__': None}
 
Teacher.__dict__的输出结果里确实有name属性 
'''
'''
    类和实例:
    和Java一样，定义类的关键字也是class
    class后面紧接着是类名，如class Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
    定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
'''
#定义Student类
class Student:
    name =''
    age = 10
    gendor = '男'

    '''
        官方推荐加self参数，表示该方法为实例方法，self在python中表示当前实例
        但是self并不是关键字，你也可以定义为this，只不过在ptyhon中规范定义为self
        __init__方法是特殊的实例方法,类似Java中的构造函数，在创建实例的时候会默认执行
        和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
        并且，调用时，不用传递该参数
    '''
    def __init__(self,name,age,gendor):
        self.name = name
        self.age = age
        self.gendor = gendor
        print('学生信息，姓名：'+self.name+"，年龄："+ str(self.age) +"，性别："+
              self.gendor)

    def do_homework(self,name):
        self.name = name
        print(self.name+'做作业')

#创建实例，直接定义会报错，有了带参的__init__方法，在创建实例的时候，就不能传入空的参数了
# student = Student()     #TypeError: __init__() missing 3 required positional
                          #arguments: 'name', 'age', and 'gendor'

student1 = Student('大雄',15,'男')    #学生信息，姓名：大雄，年龄：15，性别：男

#操作类的变量
student1.name = '小冰'

#操作类的方法
student1.do_homework(student1.name)   #小冰做作业

#通过以上代码，直接修改了student1实例的姓名，在实际开发中是不允许内部属性被外部访问的，具体看access_restriction.py文件


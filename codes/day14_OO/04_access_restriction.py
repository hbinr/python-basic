"""
    私有成员和公有成员：
    在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
    但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name属性

    如果内部属性不想被外部访问，可以把属性的名称前加上两个下划线__。这样只允许类本身访问，连子类都不可以访问。
    
    保护成员：属性的名称前加上一个下划线_，只有类及其子类可以访问。此变量不能通过from XXX import xxx 导入

"""


class Student():
    total = 0

    def __init__(self, name, age, gendor):
        self.name = name  # 公有成员
        self._age = age  # 保护成员
        self.__gendor = gendor  # 私有成员


student1 = Student('茸儿', 18, '女')

# 访问公有成员
print(student1.name)  # 茸儿
# 访问保护成员
print(student1._age)  # 18
# 访问私有成员
# print(student1.__gendor)   #AttributeError: 'Student' object has no attribute '__gendor'

# 查看student1对象的变量
print(student1.__dict__)  # {'name': '茸儿', '_age': 18, '_Student__gendor': '女'}

'''
    发现性别属性的变量名为:_Student__gendor，并不是我们显式定义的__gendor，所以在执行print(student1.__gendor)
    代码时报错了。原来是Python解释器对外把__gendor变量改成了_Student__gendor
    那如果执行print(student1._Student__gendor)呢？
'''
print(student1._Student__gendor)  # 女
'''
    私有属性还是被访问到了，那Python中访问限制有什么作用呢？还是能被外部程序访问。那么在开发中，随意访问可以吗？

    建议不要这么干，因为不同版本的Python解释器可能会把__gendor改成不同的变量名。

    总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
'''

# 私有变量的坑

student1.__gendor = '男'  # 给性别属性重新赋值
print(student1.__gendor)  # 男   这次不仅能成功访问私有变量，还能够重新赋值。。这又是怎么回事
print(student1._Student__gendor)  # 女
'''
    其实在上面的代码中已经有了答案，基于Python动态语言的特性，student1.__gendor = '男'，相当于student1对象新增了一个
    名为__gendor的变量。
    所以表面上看，外部代码“成功”地设置了__gendor变量，但实际上这个__gendor变量和class内部的__gendor变量不是一个变量！
    
'''

print(student1.__dict__)
'''
    {'name': '茸儿', '_age': 18, '_Student__gendor': '女', '__gendor': '男'}
    可以看到多了一个__gendor变量，原来的私有变量_Student__gendor并没有变化
'''

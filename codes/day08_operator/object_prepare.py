# 对象的三个特征:身份(id),值(value),类型(type)

# 1、判断身份  is或is not  id可以查其内存地址

# 2、判断值  ==

# 3、判断类型  isinstance(o,t) 第一个参数:要判断的对象或值;第二个参数:具体的对象类型
a = "hello"
print("type()判断类型,结果：", type(a))  # <class 'str'>

print("isinstance()判断类型,结果：", isinstance(a, str))  # True

# 第二个参数可以是元组，如果目标所属类型在自定义元组的范围中，则返回True  注意:list不能作为第二个参数

print("isinstance()判断类型,结果：", isinstance(a, (str, int, bool)))  # True

# print("isinstance()判断类型,结果：",isinstance(a,[str,int,bool]))   #TypeError: isinstance() arg 2 must be a type or tuple of types


# 判断类型总结：面向对象编程中，不能使用type()来判断类型，因为type()是无法判断子类的类型的

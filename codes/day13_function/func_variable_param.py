'''
    可变参数：参数数量是可变的，可以是多个，也可以没有参数
    定义函数时，有时候我们不确定调用的时候会传递多少个参数(不传参也可以)。
    此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。
'''

'''
    一、包裹位置传递
    入参会被python解析为一个tuple，所以在操作可变参数时，遍历tuple来处理
'''

def print_one(*param):
    print("入参类型为：",type(param))
    for i in param:
        print(i)

#测试1：输入普通参数
print_one(1,2,3)
#结果为：
# 入参类型为： <class 'tuple'>
# 1
# 2
# 3



'''
    二、包裹关键字传递
    入参会被python解析为一个dict
    注意遍历dict的写法
'''

def print_two(**param):
    print("入参类型为：",type(param))
    for key,value in param.items():
        print(key + ":" + str(value))

#测试：
print_two(name='小蕾', age=18, gender='女')

#结果为：
# 入参类型为： <class 'dict'>
# name:小蕾
# age:18
# gender:女


'''
    三、解包裹参数
    *和**，也可以在函数调用的时候使用，称之为解包裹(unpacking)
'''

#测试2：输入一个tuple参数
'''
    在python中，入参为tuple，可变参数可以接收tuple里的每个序号对应值，平铺入参
    但是要注意入参方式
'''
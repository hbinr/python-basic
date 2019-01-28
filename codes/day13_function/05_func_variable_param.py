'''
    可变参数：参数数量是可变的，可以是多个，也可以没有参数
    定义函数时，有时候我们不确定调用的时候会传递多少个参数(不传参也可以)。
    此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。
    
    注意：可变参数最好位于参数列表的最后
'''

'''
    一、包裹位置传递
    入参会被python解析为一个tuple，所以在操作可变参数时，遍历tuple来处理
'''

def print_one(*param):
    print("入参类型为：",type(param))
    print("入参为：",param)

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
    
    在python中，入参为tuple，可变参数可以接收tuple里的每个序号对应值，平铺入参
    但是要注意入参方式
'''
print("-------------开始解包裹参数----------------")
#测试2：输入一个tuple或list参数，不解包裹参数会出错吗？
param_tuple = (1,2,3,4)
param_list = [5,6,7,8]

#调用print_one()方法
print_one(param_tuple)    #入参为： ((1, 2, 3, 4),)
print_one(param_list)     #入参为： ([5, 6, 7, 8],)
'''
    可以发现，当入参是一个tuple时，直接入参输出一个二维元组，这显然不是我们所期待的结果，
    在python中，要想解包裹参数，必须在入参时也加上*或**
'''

#正确使用：
print_one(*param_tuple)   #入参为： (1, 2, 3, 4)
print_one(*param_list)    #入参为： (5, 6, 7, 8)


#测试3： 入参为一个dict
param_dict = {"name":"茸茸","age":18}
print_two(**param_dict)
'''
print_two(**param_dict)结果为：
入参类型为： <class 'dict'>
name:茸茸
age:18
'''
"""
    内置函数map()把一个函数func依次映射到序列或迭代器对象的每个元素上，并返回一个可迭代的map对象作为结果，map对象中
    每个元素是原序列经过函数func处理后的结果，map()函数不对原序列或迭代器做任何修改

    适用场景:

"""
# 1. 把列表中的元素转为字符串,观察map对象本质
map_one = map(str, range(10))
print(map_one)  # <map object at 0x00000298C6FCFEB8>  返回的是一个map对象,是可迭代。属于可变类型
print(type(map_one))  # <class 'map'>
for i in map_one:
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


# 2. 单参数函数映射到一个序列的所有元素上
def addOne(x):
    return x + 2


lst_one = list(map(addOne, range(5)))  # range(5)中的每个元素都执行了addDemo方法，返回的结果中每个元素都加2
print(lst_one)  # [2, 3, 4, 5, 6]


# 3. 多参数映射到多个序列上
def addMore(x, y):
    return x + y


lst_two = list(map(addMore, range(5), range(5)))  # 两个序列的每个元素按照顺序一一相加。
print(lst_two)  # [0, 2, 4, 6, 8]

'''
    如果两个序列的大小不一致会发生什么？如果能正常执行func,那么返回结果是怎样的？
    答：不一致是能正常执行的，以最小的序列为基准。如：
'''
lst_three = list(map(addMore, range(3), range(8)))
print(lst_three)  # [0, 2, 4]   以range(3)为基准，只进行了三个元素相加,其余的都舍掉了

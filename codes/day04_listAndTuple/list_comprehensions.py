'''
    列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
    配合 for 循环使用，对for循环遍历出的结果来进行操作，并在 外侧加上一个中括号，这样就可以直接生成一个 list。
'''
# 练习1：操作单个变量：  创建[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_one = [x for x in range(1, 11)]
print(list_one)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 练习2：操作多个变量： 将一个dict通过遍历组装成一个list
dict_one = {'a': 1, 'b': 2, 'c': 3}
list_two = [k + '=' + str(v) for k, v in dict_one.items()]
print(list_two)  # ['a=1', 'b=2', 'c=3']

# 练习3：还可以配合if来使用，如下提取出 1-10 中偶数数字
list_three = [y for y in range(1, 11) if y % 2 == 0]
print(list_three)  # [2, 4, 6, 8, 10]

# 练习4：支持 多重循环
list_four = [x + y for x in "abc" for y in "xyz"]
print(list_four)  # ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']

# for x in 'abc':
#     for y in 'xyz':
#         x+y

# 练习5: 生成一个新列表，满足:其元素为元组，且元组组成为(偶数,奇数)
newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newlist)

# 练习6：带if else  [exp1 if condition else exp2 for x in data] 
# 此处if…else主要起赋值作用，当data中的数据满足if条件时将其做exp1处理，否则按照exp2处理，最后统一生成为一个数据列表

# 1-100中，不是3的倍数的数去相反数，其余的数保持不变
q = [x if x % 3 == 0 else -x for x in range(10)]
print(q)

# 薪资大于5000则加500，反之加200
dict1 = {'name': 'Tom', 'salary': 10000}
dict2 = {'name': 'Bob', 'salary': 5000}
list_five = [dict1, dict2]


def func():
    newlist = []

    for i in list_five:
        j = {}
        if i['salary'] > 5000:
            i['salary'] + 200
            newlist.append(i)
        else:
            i['salary'] + 500
            newlist.append(i)

    print(newlist)


func()

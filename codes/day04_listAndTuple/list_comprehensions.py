'''
    列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
    配合 for 循环使用，对for循环遍历出的结果来进行操作，并在 外侧加上一个中括号，这样就可以直接生成一个 list。
'''
#练习1：操作单个变量：  创建[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_one = [x for x in range(1,11)]
print(list_one)   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#练习2：操作多个变量： 将一个dict通过遍历组装成一个list
dict_one = {'a':1,'b':2,'c':3}
list_two = [k +'='+ str(v) for k,v in dict_one.items()]
print(list_two)      #['a=1', 'b=2', 'c=3']

#练习3：还可以配合if来使用，如下提取出 1-10 中偶数数字
list_three = [y for y in range(1,11) if y%2 == 0]
print(list_three)    #[2, 4, 6, 8, 10]


#练习4：支持 多重循环
list_four = [x+y for x in "abc" for y in "xyz"]
print(list_four)     #['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']

# for x in 'abc':
#     for y in 'xyz':
#         x+y
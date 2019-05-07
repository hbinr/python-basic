__all__ = ["list","tuple","set","dict"]   #dict模块的内置变量
#dict 字典  dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

#dict也是集合，所以在定义时也是使用"{}"来表示，和set不同的是：增加了key-value的概念，dict也是无序不重复的，key的值不允许重复

#dict是用哈希表实现的，哈希表（Hash table）

#key:必须是不可变的类型，如：number:1str:"1"
#    这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
#    这个通过key计算位置的算法称为哈希算法（Hash）。要保证hash的正确性，作为key的对象就不能变。

#value:可以是任意类型，甚至是dict本身

#一、定义
#1、空字典  {}
print(type({}))    #<class 'dict'>

#2、简单定义,字典的key并不是固定的，同一个
print({1:1,"1":1113,"study":"python"})         #{1: 1, '1': 1113, 'study': 'python'}

#3、嵌套定义  value值可以存放任意数据类型
list_test = [1,2,True]
tuple_test = (1,"hello","world",72j)
set_test = {1,2,3}
dict_test = {1:"one",2:200,"404":"Not found"}
print({"1":"one","list":list_test,"tuple":tuple_test,"set":set_test,"dict":dict_test})   #{'1': 'one', 'list': [1, 2, True], 'tuple': (1, 'hello', 'world', 72j), 'set': {1, 2, 3}, 'dict': {1: 'one', 2: 200, '404': 'Not found'}}

#注意：字典的key是不允许重复的，如果重复了，则默认是最后一次存储的数据，之前的值会被冲掉
print({"one":"Java","one":"Python","two":"Golang"})   #{'one': 'Python', 'two': 'Golang'}

#字典的value值则可以重复，同一个value可有多个key
print({"one":"Java","two":"Java","three":"Java"}) #{'one': 'Java', 'two': 'Java', 'three': 'Java'}

#4、键必须不可变，所以可以用数字，字符串或元组充当，用列表就不行，如下实例：
testTuple = {(1,2):"Tulple"}  
print(testTuple)      #{(1, 2): 'Tulple'}
# testList = {[1,2,3]:"List"}
# print(testTuple)      #报错  TypeError: unhashable type: 'list'

#二、操作
dict1 = {1:"one",2:"two",}
dict2 = {"java":"java","python":"python","Go":"Golang"}
#1、 取值 就是在后面加上对应的key值即可，但是不支持切片操作
print(dict1[2])    #two
# print(dict[2:])  #TypeError: unhashable type: 'slice'

#2、新增值,直接操作dict
dict1["3"] ="新增的"
print(dict1)       #{1: 'one', 2: 'two', '3': '新增的'}

#3、判断key是否存在 in、not in
print("java" in dict2)  #True  判断是否存在 key->"java"，而不是判断value值
print("22" in dict2)    #False

# 三、函数操作
#1、len  取大小
print(len(dict1))  #2

#2、get() 获取值。另外，除了用in、not in外，还可以用get()来判断key是否存在  如果key不存在，返回None，或者自己指定的value
print("dict1的key为1时,其对应的值为："+dict1.get(1))   #dict1的key为1时,其对应的值为：one
print("dict1的key为2时,其对应的值为："+dict1.get(2))   #dict1的key为2时,其对应的值为：two

print(dict1.get(3))  #注意：返回None的时候Python的交互环境不显示结果，并不是不存在这样的值，下一行代码可以证明
# print("dict1的key为3时,其对应的值为："+dict1.get(3))   #报错 TypeError: must be str, not NoneType，  None不是字符串类型

#key不存在，返回自己指定的value
print(dict1.get(3,"不存在key为3的数据"))  #不存在key为3的数据


#3、update() 修改 用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，
# 则该元素只会出现一次，重复的会忽略。
dict3 = {"name":"Tom","age":"20"}
dict4 = {"sex":"male"}
print(dict3)
dict4.update(dict3)
print(dict4)    #{'sex': 'male', 'name': 'Tom', 'age': '20'}



#4、copy()  返回字典对象的浅复制
dict_copy = dict3
dict3.update({'test':'copy'})
print('原字典为:',dict3,"复制后的字典为:",dict_copy)

#原字典为: {'name': 'Tom', 'age': '20', 'test': 'copy'} 复制后的字典为: {'name': 'Tom', 'age': '20', 'test': 'copy'}
'''
    dict3新增了一个{'test':'copy'},为啥dict_copy的也同时新增了？
    dict_copy = dict3   这行代码表示的是：dict_copy和dict3指向同一个字典。该字典在内存的值是一致的，内存里的值发生改变，两个
    变量都会得到体现
    扩展：对于dict3 = {"name":"Tom","age":"20"}变量，如果使用copy()函数，会发生什么情况呢？

    copy() 返回字典对象的浅复制。所谓浅赋值，是指生成一个新的列表，并且把原列表中的所有元素的引用都复制到新列表中。如果原列表中只包含
    整数、实数、复数等基本类型或元组、字符串这样的不可变类型的数据，一般是没有问题的。但是如果原列表中包含列表之类的可变数据类型，由于
    浅复制是只是把子列表的引用复制到新列表中，于是修改任何一个都会影响到另外一个。
    如以下代码：
'''
x = [1,2,[1,2,3]]               #原列表中包含子列表，且第三个元素是list(可变数据类型)
y = x.copy()
print('浅复制后的列表为:',y)     #赋值后的列表为: [1, 2, [1, 2, 3]]
y[2].append(4)                  #修改复制列表中的子列表。x列表是否会发生变化？？
print('原列表为:',x,'浅复制后的列表为:',y)    #原列表为: [1, 2, [1, 2, 3, 4]] 浅复制后的列表为: [1, 2, [1, 2, 3, 4]]
'''
    根据输出结果可以发现，原列表发生了变化，其第三个元素子中也多了个4的值。
    这就是浅复制带来的影响：通常是修改新的是列表时，把原来的也改变了，但是我们是不希望原来的列表发生改变的
    如果要避免浅复制或者直接赋值带来的影响，可以直接调用cpoy库中的deepcopy()函数实现深复制。
    所谓深复制，是值对原列表中的元素进行递归，把所有的值都复制到新列表中，对嵌套的子列表不再是复制引用。这样一来，新列表和原列表相互独立，
    修改任何一个都不会影响另外一个。
'''
#5、pop() 删除  不同于set集合，dict的删除是pop()，而不是remove()
print(dict1)   #删除前：{1: 'one', 2: 'two', '3': '新增的'}

dict1.pop("3")

print(dict1)   #删除后：{1: 'one', 2: 'two'}
#6、del 删除字典
del dict3['name']
print("删除字典dict3中key为name的元素,最后结果为：",dict3)   #删除字典dict3中key为name的元素,最后结果为： {'age': '20'}

del dict3 
# print("dict3被删除。",dict3)   #执行该语句会报错，因为dict3已经被删除了
'''
Traceback (most recent call last):
  File ".\dict.py", line 90, in <module>
    print("dict3被删除。",dict3)
NameError: name 'dict3' is not defined
'''


#四、多种方式申明字典
#1、直接显示定义
dict5 = {"java":"java","python":"python","Go":"Golang"}

#2、dict()函数  变量直接赋值或者通过嵌套序列(列表、元组的组合)来生成字典
dict6 = dict(a = 1,b = 2,c = 3) 
print(dict6)   #{'a': 1, 'b': 2, 'c': 3}  变量直接赋值


# list_01 = [[1,2,3],['Tom','Jerry']]  错误代码，执行会报错
list_01 = [[1,2],['Tom','Jerry']]

print('list_01转为字典：',dict(list_01))   #list_01转为字典： {1: 2, 'Tom': 'Jerry'}

'''
    需要特别注意的是，再通过嵌套序列转为字典时，内层的序列必须是2个，否则会报错：
    Traceback (most recent call last):
    File ".\dict.py", line 109, in <module>
    print('list_01转为字典：',dict(list_01))
    ValueError: dictionary update sequence element #0 has length 3; 2 is required
'''

#3、dict.fromkeys()  只有key时，直接生成一个字典
keys = ['a','b','c']
dict7 = dict.fromkeys(keys)    #入参只有key时，默认生成值都为:None的字典
print(dict7)   #{'a': None, 'b': None, 'c': None}   

dict7 = dict.fromkeys(keys,"hello")    #入参有key，value时，生成值都为:hello的字典
print(dict7)   #{'a': 'hello', 'b': 'hello', 'c': 'hello'}



#五、字典的元素访问

# 1. print(dic[1])  # 不能用序列的索引方式
# 字典里面也就同样的意思，但字典没有顺序，以key来作为指向，所以指向的key必须存在
dic = {'a':1, "b":2, "c":3}
print(dic['a'])     #1


# 2. 对于嵌套字典，输出嵌套内容，通过重复指向来输出
poi = {'name':'shop', 'city':'shanghai', 'information':{'address':'somewhere', 'num':66663333}}
print(poi['information']['address'])   #somewhere


# 3. get(key)方法：直接查看key的value，如果没有相应key则返回None，添加print参数可以多返回一个值
print(poi.get('c'))  #3
print(poi.get('d'),print("没有值"))  #没有值
                                     #None None 为什么会输出两个None???
# 4. keys()方法：输出字典所有key，注意这里的输出内容格式是视图，可以用list()得到key的列表，类似range()
print(poi.keys())          #dict_keys(['a', 'b', 'c'])
print(type(poi.keys()))    #<class 'dict_keys'>
print(list(poi.keys()))    #['name', 'city', 'information']   所有key组成的列表
'''
    <class 'dict_keys'>
    在Python2里，keys()会返回一个列表.
    而在Python3中则会返回dict_keys()，它是键的迭代形式。
    这种返回形式对于大型字典非常有用，因为它不需要时间和空间来创建返回的列表。有
    时你需要的可能就是一个完整的列表，但在Python3中，你只能自己调用list()将dict_keys转换为列表类型。
'''

# 5. values()方法：输出字典所有values，原理同.keys()方法
print(poi.values())        #dict_values(['shop', 'shanghai', {'address': 'somewhere', 'num': 66663333}])
print(type(poi.values()))  #<class 'dict_values'>

# 6. items()方法：输出字典所有items(元素) 原理同.keys()方法,输出形式为嵌套序列,列表和元组的组合
# print(poi.items())         #dict_items([('name', 'shop'), ('city', 'shanghai'), ('information', {'address': 'somewhere', 'num': 66663333})])
print(type(poi.items()))   #<class 'dict_items'>

#六、字典的遍历
# 1. 遍历key
for k in poi:  #同for k in poi.keys(): 

    print(k, end=' ')   #name city information  
print()
# 2. 遍历value
for v in poi.values():
    print(v, end=' ')   #shop shanghai {'address': 'somewhere', 'num': 66663333}
print()
# 3. 同时遍历key,value
for k, v in poi.items():
    #print('key = ', k, ',', 'value = ', v)  写法并不简洁,且没有pythonic,改为以下写法:
    print('key = %s, value = %s' %(k, v))
    

'''
输出结果:
key =  name , value =  shop
key =  city , value =  shanghai
key =  information , value =  {'address': 'somewhere', 'num': 66663333}
'''


# 七 练习
# 1.dict.keys()生成的是不是列表？ 

'''
    dict.keys()生成的并不是列表,而是key视图.可以通过list()函数将结果转为列表
'''

# 2.如何判断一个value是否存在于字典中？
print('shop' in poi.values())     #True

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
list = [1,2,True]
tuple = (1,"hello","world",72j)
set = {1,2,3}
dict = {1:"one",2:200,"404":"Not found"}
print({"1":"one","list":list,"tuple":tuple,"set":set,"dict":dict})   #{'1': 'one', 'list': [1, 2, True], 'tuple': (1, 'hello', 'world', 72j), 'set': {1, 2, 3}, 'dict': {1: 'one', 2: 200, '404': 'Not found'}}

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
dict4.update()
print(dict4)    #{'sex': 'male', 'name': 'Tom', 'age': '20'}



#4、pop() 不同于set集合，dict的删除是pop()，而不是remove()

print(dict1)   #删除前：{1: 'one', 2: 'two', '3': '新增的'}

dict1.pop("3")

print(dict1)   #删除后：{1: 'one', 2: 'two'}
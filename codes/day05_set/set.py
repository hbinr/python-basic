#set 用'{}'来定义，是【无序不重复】元素集，也无法通过数字进行索引，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

#一、定义
print({1,2,3,'str'})         #{1, 2, 3, 'str'}

print({1,2,3,'str',2,True})  #{1, 2, 3, 'str'}
print({1,2,3,'STR',2,True})  #{1, 2, 3, 'STR'}

print({True,2})              #{True, 2}  TODO
print({2,True})              #{True, 2}

print({True})                #{True}  TODO
print({True,True})           #{True}
#空集合
print(type({}))   #<class 'dict'>

print(type(set()))  #<class 'set'> 虽然集合在python的定义是使用'{}'来界定的，但是定义一个空集合，并不是'{}'，而是set()


#无序
# {1,2,3,4}[0]  #TypeError: 'set' object does not support indexing, 不支持序号，所以是无序的
#不重复
print({1,2,2,3,3,3,3,4,4})  #{1, 2, 3, 4}

#二、操作
set1 = {1,2,3,4,5}
set2 = {3,4,7}
#1、不支持切片操作
# set1[1:2]   #TypeError: 'set' object is not subscriptable

#2、in、not in
print(1 in set1)  #True
print(6 not in set1)  #True

#3、集合的差集  '-'，去除集合中的重复元素,求差集（项在set1中，但不在set2中）
print(set1 - set2)    #{1, 2, 5}

#4、集合的交集  '&'，取集合公共的部分
print(set1 & set2)    #{3, 4}
# print(set1 && set2) #SyntaxError: invalid syntax 语法错误， &&表示逻辑与，不能用于集合的取交集运算

#5、集合的并集  '|'，合并两个集合
print(set1 | set2)   #{1, 2, 3, 4, 5, 7}

#6、 对称差集   '^'，（项在set1或set2中，但不会同时出现在二者中）
print(set1 ^ set2)   #{1, 2, 5, 7}

#实际问题：怎么去除海量列表里重复元素？
a = [11,2,2,2,2,33,3,33,3,444,44,4,4,4,44,4]
b = set(a);
print(b)  #{33, 2, 3, 4, 11, 44, 444}  此时已经求掉了重复元素，但是结果是一个set集合，实际中想要的是一个list
c = [i for i in b]  #便利集合,将获取的值存到c列表中
print(c)  #[33, 2, 3, 4, 11, 44, 444]
# 三、函数操作
#1、len  取大小
print(len(set1))  #5

#2、add  添加
set1.add("Hello")
print(set1)   #{1, 2, 3, 4, 5, 'Hello'} ，追加
#3、update 修改  update() 方法用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，
# 则该元素只会出现一次，重复的会忽略。
set1.update(set2)
print(set1)          #{1, 2, 3, 4, 5, 'Hello', 7}
print(set1 | set2)   #{1, 2, 3, 4, 5, 'Hello', 7}    update()和取并集的结果是一致的
print(set1 == set1|set2)   #True   set1.update(set2)执行后,set1  ==  set1 | set2
#4、remove 删除
set1.remove(1)
print(set1)   #{2, 3, 4, 5, 'Hello', 7}

#5、最大,最小元素
print(max(set2))  #7
print(min(set2))  #3
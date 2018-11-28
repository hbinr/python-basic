# List（列表） 是 Python 中使用最频繁的数据类型。
#
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
#
# 列表用 [ ] 标识，是 python 最通用的复合数据类型。
#
# 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

#一、定义
#简单定义
print([1,2,3])  #[1, 2, 3]

print([]) #[] 空列表

#混合定义,支持number类型  字符串类型等
print([1,'2',3.222,4j,True])  #[1, '2', 3.222, 4j, True]

#嵌套定义    Java中成为二维数组，在python中称为嵌套列表
print([[1,2],[3,True],[4,"Hello"],[5,6.00,89j],])  #[[1, 2], [3, True], [4, 'Hello'], [5, 6.0, 89j]]

#二、运算
list = [1,2.50,'Hello',True,7j]

#1、获取某个元素  下标从0开始
print(list[2])  # Hello
print(list[-1]) #7j
print(list[0:3]) #[1, 2.5, 'Hello']

#2、+, *, in, not in
print(list+list) #[1, 2.5, 'Hello', True, 7j, 1, 2.5, 'Hello', True, 7j]
print([1,2] + ['s','2']) #[1, 2, 's', '2'],不同类型的列表可以相加

print(list*2) #[1, 2.5, 'Hello', True, 7j, 1, 2.5, 'Hello', True, 7j]
# print(list*2.5) #TypeError: can't multiply sequence by non-int of type 'float'

print(2 in list) #False
print(2 not in list) #True

#3、修改，列表是可以根据下标来修改元素的
list[0] = '2'
print(list) #['2', 2.5, 'Hello', True, 7j] ,第一位变为了'2'


#三、列表的函数
#1、len()表示列表的大小,返回值为int
print(len(list)) #5

#2、max() min() 最大、最小
# print(max(list))  # 报错  TypeError: '<' not supported between instances of 'float' and 'str'  不同的数据类型无法进行比较
print(max([1,2,4,99]))  #99
print(max(['a','2','4','A'])) #a:97，2:50，4:52，A:65。比较ASCII值  ord('2')
print(ord('4'))

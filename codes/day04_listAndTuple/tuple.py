# Python的元组与列表类似，不同之处在于元组的元素不能修改。
#
# 元组使用小括号，列表使用方括号。
#
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
#
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
#
#


# 一、定义
# 元组中只包含一个元素时，需要在元素后面添加逗号,不加逗号的话，python会把'()'当作算术运算符来处理
print((1,))  # (1,)  单个元素
print(('1'))  # 1
print((2))  # 2
print((True))  # True

# 简单定义
print((1, 2, 3))  # (1, 2, 3)

print(())  # () 空元组

# 混合定义,支持number类型  字符串类型等
print((1, '2', 3.222, 4j, True))  # (1, '2', 3.222, 4j, True)

# 嵌套定义   嵌套元组
print(((1, 2), (3, True), (4, "Hello"), (5, 6.00, 89j),))  # ((1, 2), (3, True), (4, 'Hello'), (5, 6.0, 89j))

# 二、运算
tuple = (1, 2.50, 'Hello', True, 7j)

# 1、获取某个元素  下标从0开始
print(tuple[2])  # Hello
print(tuple[-1])  # 7j

# 2、+, *, in, not in
print(tuple + tuple)  # (1, 2.5, 'Hello', True, 7j, 1, 2.5, 'Hello', True, 7j)
print((1, 2) + ('s', '2'))  # (1, 2, 's', '2'),不同类型的元组可以相加

print(tuple * 2)  # (1, 2.5, 'Hello', True, 7j, 1, 2.5, 'Hello', True, 7j)
# print(tuple*2.5) #TypeError: can't multiply sequence by non-int of type 'float'

print(2 in tuple)  # False
print(2 not in tuple)  # True

# 3、不允许修改
# tuple[0] = '2'  #TypeError: 'tuple' object does not support item assignment


# 三、元组的函数
# 1、len()表示元组的大小,返回值为int
print(len(tuple))  # 5
# 2、max() min() 最大、最小
# print(max(tuple))  # 报错  TypeError: '<' not supported between instances of 'float' and 'str'  不同的数据类型无法进行比较
print(max((1, 2, 4, 99)))  # 99
print(max(('a', '2', '4', 'A')))  # a  比较ASCII值

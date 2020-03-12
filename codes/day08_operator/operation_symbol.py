# Python运算符有：算术运算符、赋值运算符、比较(关系)运算符、逻辑运算符、成员运算符、身份运算符、位运算符

# 所有变量的位操作都是通过强制转换成bool实现的，并且表达式的值是从左到右第一个能够确定表达式的值的变量


# 一、算术运算符 + - * / % // **
print(5 % 2)  # 1
print(2 ** 2)  # 4  2的2次方
print(2 ** 5)  # 32  2的5次方

# 二、赋值运算符   = , += , -= , *= , /= , %= , //= , **=
a = 1
a = a + 1  # 2 相当于a+=1，值得注意的是在python中是没有++或者--这两个运算符

b = 2
b **= 3  # 8
print(b)

# 三、比较(关系)运算符 ,返回结果为bool类型   == , != , > , < , >= ,<=
b += b >= 2  # 9   先执行 b>=2 结果为True，然后执行b = b + True，即8 + int(True)1
print(b)
# 并不是只有数字才能做比较运算
print('a' > 'b')  # False  ,实际比较得ASCII值
ord('a')  # 97
ord('b')  # 98   但是ord()是作用于单字符的。如果是字符串比较呢？

print('abc' >= 'abd')  # False  ，字符串按位比较，两个字符串第一位字符的ascii码谁大，字符串就大，不再比较后面的；第一个字符相同就比第二个字符串，
# 以此类推，需要注意的是空格的ascii码是32，空（null）的ascii码是0

print([1, 3, 2] > [1, 2, 5])  # True  ，1 > 1为False;3 > 2为True;2 > 5为False  结果怎么返回True？？详见：notes -> list比较源码分析
# print((1,3,2) > [1,2,5])  #TypeError: '>' not supported between instances of 'tuple' and 'list'
print((1, 3, 2) > (1, 2, 5))  # True

# 四、逻辑运算符 ,返回结果为bool类型   and  , or  , not
# 1、and  且  都为True(Flase)，结果才为True(False)
flag = True and True
print("True and True 的结果：", flag)  # True

flag = True and False
print("True and False 的结果：", flag)  # False

flag = False and False
print("False and False 的结果：", flag)  # False

# 2、or  或  只要有一个为True，结果就为Tue；都为False时，结果才为False
flag = True or True
print("True or True 的结果：", flag)  # True

flag = True or False
print("True or False 的结果：", flag)  # True

flag = False or False
print("False or False 的结果：", flag)  # False

# 3、not  非
flag = not True
print("not True 的结果：", flag)  # False

flag = not False
print("not True 的结果：", flag)  # True

flag = not not False
print("not not False 的结果：", flag)  # False

# 4、并不是只有bool类型才能做逻辑运算
flag = '1' and 2
print("'1' and 2 做逻辑运算 结果：", flag)  # 2  and是要全部为真才为真，所以and返回的是最后一个判断为true的值

flag = 'hello' or 2
print("'hello' or 2 做逻辑运算 结果：", flag)  # "hello"  即True  or是要只要有真结果就为真，所以or返回的是第一个判断为true的值，之后的值就不再判断了

flag = [] or {1, 2, 3}
print("[] or {1,2,3} 做逻辑运算 结果：", flag)  # {1, 2, 3}  即True

flag = set() and {}
print("set() and {} 做逻辑运算 结果：", flag)  # set() 即False
# 总结一句话就是：无论操作符是哪个，最后的结果一定是按照计算顺序能最快判断出结果的那个表达式决定的

# 五、成员运算符 ,返回结果为bool类型   in , not in
list = [1, 2, 3, "one", "two"]
flag = 1 in list
print("成员运算符 'in' 结果：", flag)  # True

flag = 'three' not in list
print("成员运算符 'not in' 结果：", flag)  # True

# 注意：用于字典时,成员运算符作用的是  key
dict = {1: "one", "2": "two"}
flag = 1 in dict
print("成员运算符用于字典时, 1 结果为：", flag)  # True
flag = "one" in dict
print("成员运算符用于字典时,'one' 结果为：", flag)  # False
# 六、身份运算符 ,  返回结果为bool类型   is, is not
a = 1
b = "1"
flag = a is b
print("身份运算符 'is' 的结果：", flag)  # False  比较的是地址，并不是值

a = {1, 2, 3}
b = {2, 1, 3}
flag = a == b
print("两个集合比较,关系运算符 '==' 的结果：", flag)  # True   a,b两个集合的元素顺序都不一样，为什么结果为True呢？
# 因为集合是无序的，且'=='比较的是值，所以a == b
flag = a is b
print("两个集合比较,身份运算符 'is' 的结果：", flag)  # False  is运算符比较的是地址
print(id(a))  # a的地址为：38576872
print(id(b))  # a的地址为：44670312   可见，两个集合的地址都不一样，所以a is b的结果为False

c = (1, 2, 3)
d = (2, 1, 3)
flag = c == d
print("两个元组比较,关系运算符 '==' 的结果：", flag)  # False   c,d为元组，而元组是有序的，所以结果为False
flag = c is b
print("两个元组比较,身份运算符 'is' 的结果：", flag)  # False  is运算符比较的是地址
print(id(c))  # a的地址为：38576872
print(id(d))  # a的地址为：44670312   可见，两个集合的地址都不一样，所以a is b的结果为False

# 七、 位运算符   & , | , ^ , ~ , << , >>   把数字当作二进制数进行运算
i = 2
j = 3
# 1、&  按位与： 比较二进制数的每一位，如果都为1，则返回1，其他情况返回0
print("2转换为二进制数:", bin(i))  # 0b10
print("3转换为二进制数:", bin(j))  # 0b11

print("按位与运算:", bin(i & j))  # 0b10

# 2、|  按位或： 比较二进制数的每一位，只要有一个数字为1，则返回1，其他情况返回0
print("按位或运算:", bin(i | j))  # 0b11

# 3、^  按位异或： 比较二进制数的每一位，当前位的两个二进制表示不同则为1相同则为0.该方法被广泛推广用来统计一个数的1的位数！
print("按位异或运算:", bin(i ^ j))  # 0b1
print(0b1 == 0b01)  # True
# 4、~

# 5、<<  左移运算符m<<n表示吧m左移n位。左移n位的时候，最左边的n位将被丢弃，同时在最右边补上n个0.


# 6、>>  　右移运算符m>>n表示把m右移n位。右移n位的时候，最右边的n位将被丢弃。但右移时处理最左边位的情形要稍微复杂一点。
# 这里要特别注意，如果数字是一个无符号数值，则用0填补最左边的n位。如果数字是一个有符号数值，则用数字的符号位填补最左边的n位。
# 也就是说如果数字原先是一个正数，则右移之后再最左边补n个0；如果数字原先是负数，则右移之后在最左边补n个1.

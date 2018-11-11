#一、python中可以用以下方式表示字符串，这些引号用来表示字符串时时成对出现的

#单引号 '
print('hello world')
#双引号 "
print("hello world")
#三引号 '''  常用来表示换行字符
print("hello world")
str = '''sssssssssssssssssssssssssssssssss,sssssssssssssssssssss
ssssssssssssssssssssssssssssssss.2222222222222222222222'''
print("用三引号表示多行字符串"+str)

#打印let's go的方式
print('let\'s go') #使用单引号，需要加转义字符 '\'
print("let's go") #使用双引号
print('''let's go''') #使用三引号


#二、字符串的运算
operateStr = "Hello World"
#1、获取某个字符
print(operateStr[0])#结果为H,下标为0的字符

#2、使用[:]来获取想要的字符串，相当于Java中的数组操作，Java中，字符串地层也是数组实现的
print(operateStr[0:5])#结果为Hello，数字为字符所在的下标位置(左开右闭)

#获取World
print(operateStr[6:]) #正向 切片操作
print(operateStr[6:11]) #正向
print(operateStr[-5:]) #逆向  '-'表示从末尾开始，下标为从1开始 ，
print("2222"+operateStr[-5:-0]) #结果为2222，不存在'-0'位

#3、运算  +:字符串连接; * :重复输出字符串 （没有-和/）;   in如果字符串中包含给定的字符返回 True，反之not in
print(operateStr+operateStr); #Hello WorldHello World
# print('A'+1) #TypeError: can only concatenate str (not "int") to str，不同类型的对象不可以相加

print(operateStr*3) #Hello WorldHello WorldHello World
# print(operateStr*3.5) #TypeError: can't multiply sequence by non-int of type 'float'

print('H'in operateStr) #True
print('H'not in operateStr) #False

#4、r/R 表示原始字符串
print(R'\n') # \n
print(r'\n') # \n

#5、% 格式字符串    %s:格式化字符串;  %d:格式化整数  等
print("My name is %s and weight is %d kg!" % ('Zara', 21))

#6、不允许修改字符串
# operateStr[0] = 10  #TypeError: 'str' object does not support item assignment


#三、字符串的函数
#1、len()表示字符串的大小,返回值为int
print(len(operateStr)) #11
#2、max() min() 最大、最小
print(max(operateStr))  # r
print(ord('r'))  #r的ASCII的值为114
print(ord('W'))  #W的ASCII的值为87
print(ord('w'))  #W的ASCII的值为119   小写字母的ASCII值的=大写ASCII值+32
print(min(operateStr))  # '' 返回空格
#print(ord(1))  #报错 入参必须为str,且是单个字符
print(ord('1'))  #49
# print(ord('11')) #报错  TypeError: ord() expected a character, but string of length 2 found ,ord()希望得到一个字符，但是找到了长度为2的字符串

# ord()源码
# def ord(*args, **kwargs): # real signature unknown
#     """ Return the Unicode code point for a one-character string. """
#     pass

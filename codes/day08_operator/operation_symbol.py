#Python运算符有：算术运算符、赋值运算符、比较(关系)运算符、逻辑运算符、成员运算符、身份运算符、位运算符


#一、算术运算符 + - * / % // **
print(5%2)   #1
print(2**2)  #4  2的2次方
print(2**5)  #32  2的5次方

#二、赋值运算符   = ，+=，-=，*=，/=，%=，//=，**=
a = 1
a = a + 1  #2 相当于a+=1，值得注意的是在python中是没有++或者--这两个运算符

b = 2
b**=3  #8
print(b)

#三、比较(关系)运算符 ,返回结果位bool类型   == 、!= 、> 、< 、>= 、<=
b += b >= 2   #9   先执行 b>=2 结果为True，然后执行b = b + True，即8 + 1
print(b)
#并不是只有数字才能做比较运算
print('a' > 'b')  #False  ,实际比较得ASCII值
ord('a')    #97
ord('b')    #98   但是ord()是作用于单字符的。如果是字符串比较呢？

print('abc' >= 'abd')    #False  ，在python中，字符串比较时，是单个字符一一去比较

print([1,3,2] > [1,2,5])    #True  ，1 > 1为False;3 > 2为True;2 > 5为False  结果怎么返回True？？
# print((1,3,2) > [1,2,5])  #TypeError: '>' not supported between instances of 'tuple' and 'list'
print((1,3,2) > (1,2,5))    #True
#四、逻辑运算符 ,返回结果位bool类型   and   or   !
#1、and  且  都为True(Flase)，结果才为True(False)
flag = True and True
print("True and True 的结果：",flag)  #True

flag = True and False
print("True and False 的结果：",flag)  #False

flag = False and False
print("False and False 的结果：",flag)  #False

#2、or  或  只要有一个为True，结果就为Tue；都为False时，结果才为False
flag = True or True
print("True or True 的结果：",flag)  #True

flag = True or False
print("True or False 的结果：",flag)  #True

flag = False or False
print("False or False 的结果：",flag)  #False

#3、not  非
flag = not True
print("not True 的结果：",flag)  #False

flag = not False
print("not True 的结果：",flag)  #True

flag = not not  False
print("not not False 的结果：",flag)  #False
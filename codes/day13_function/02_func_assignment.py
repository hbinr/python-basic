'''
    记录Python序列解包和链式赋值
    序列解包：当函数或方法返回元组时，将元组中值赋给变量序列中的变量，这个过程就叫做序列解包
    链式赋值：一种简易型批量赋值语句，一行代码即可为多个变量同时进行赋值
'''

#一、序列解包
#先定义三个变量，并赋值
# a = 1
# b = 2
# c = 3
#python中更简洁的写法
a, b, c = 1, 2, 3
print(a, b, c)        #1 2 3    值一一对应赋值到a,b,c中

#1、序列1，2，3被打包到元组values中
values = 4,5,6
#values是一个元组
print(type(values))   #<class 'tuple'>

#2、序列解包，元组values中的值分别被赋给变量序列中的x,y,z
x, y, z = values      #本质上这个操作就相当于上面a,b,c = 1,2,3的操作

print(x, y, z)        #4 5 6

#思考：赋值的时候，两边对等，正常赋值。那不对等的时候，可以正常赋值吗，是全部不赋值还是赋值一部分？以下进行验证
# a, b = (1,2,3)        #ValueError: too many values to unpack (expected 2)
#但是在python3.0出现了序列解包后，就不存在这样的情况，不过语法糖有点变化，需要加 '*'
a, *b = (1,2,3)
print(a,b)            #1 [2, 3]，类似可变参数的传值
*a, b = (1,2,3)
print(a,b)            # [1, 2] 3  '*'的位置是自由的

#练习：假如一个字符串'ABCDEFGH'，要输出下列格式:见图：pictures/序列解包练习.png
#     即: 每次取出第一个作为首，然后余下的字符串拆成列表，放置在后面
#     原博客：https://blog.csdn.net/Jerry_1126/article/details/78510847
s = 'ABCDEFGH'

#不用序列解包的解法
while s:
    front, s = s[0],list(s[1:])     #front  每次都取出第一个
                                    #s  取序号为1后的所有值并转换为list，然后赋值给新的s
    print(front, s)

#使用序列解包
s2 = 'ABCDEFGH'
while s2:
    front, *s2 = s2
    print(front, s2)
#结果：
# A ['B', 'C', 'D', 'E', 'F', 'G', 'H']
# B ['C', 'D', 'E', 'F', 'G', 'H']
# C ['D', 'E', 'F', 'G', 'H']
# D ['E', 'F', 'G', 'H']
# E ['F', 'G', 'H']
# F ['G', 'H']
# G ['H']
# H []


#二、链式赋值
m = 1
n = 1
q = 1

#上述定义可以写为:
m=n=q= 1

'''
链式赋值是一种非常优雅的赋值方式，简单、高效且实用。但同时它也是一个危险的糖衣炸弹
'''
#练习:求链式赋值语句中变量 x 的值？
x = [1, 2, 3, 4, 5]
j = 0
j = x[j] = 3

print("变化后的List:",x)      #[1, 2, 3, 3, 5]
print("j的值为：",j)          #j的值为： 3
'''
    看：https://blog.csdn.net/jmilk/article/details/78733409
    如果你有过 C 语言的编程经验，那么你的思维习惯可能会让你得出这样的结果：x[0] 被赋值为 3，然后 j 再被赋值为 3，所以变量 x 的值为 [3, 2, 3, 4, 5]。
但实际上正确的答案却是：变量 j 首先被赋值为 3，然后 x[3] 再被赋值为3，所以最终变量 x 的值为 [1, 2, 3, 3, 5]。
从上述结果的表现可以看出二者的区别为：C 语言的赋值顺序是 自右往左， 依次进行的，而 Python 则相反。* 
造成这种表征区别的本质原因是由于 C 语言是一种「值语义」类型语言，而 Python 是「对象语义」类型语言。
--------------------- 
作者：范桂飓 
来源：CSDN 
原文：https://blog.csdn.net/jmilk/article/details/78733409 
版权声明：本文为博主原创文章，转载请附上博文链接！    

'''

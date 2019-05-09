'''
    lambad表达式常用来声明匿名函数，即没有函数名字的临时使用的小函数，常用在临时需要一个类似于函数的功能但又不想
    定义函数的场合。
    lambda表达式只可以包含一个表达式，不允许包含其他复杂的语句，但在表达式中可以调用其他函数，该表达式的计算结果
    相当于函数的返回结果。
    lambda 参数: 逻辑
'''
import random
# 1. 简单小例子
f = lambda x, y, z: x + y + z    #也可以给 lambda 表达式起个名字
print(f(1,2,3))

# 2. 支持默认值参数
g = lambda x, y = 1, z = 2: x + y + z
print(g(1))             #4
print(g(1,y=3,z=4))     #8 调用时使用关键字参数赋值

# 3. 在可变类型中使用lambda表达式
lst = [(lambda x:x**2), (lambda y:y**2), (lambda z:z**2)]
print(lst[0](2), lst[1](3), lst[2](3))          #4 9 9

# dic = {'f1':lambda :1 + 2, 'f2':lambda :2 + 3, 'f3':lambda :3 + 4}
dic = {'f1':(lambda :1 + 2), 'f2':(lambda :2 + 3), 'f3':(lambda :3 + 4)}   #方便阅读还是给lambda表达式加上'()'较好
print(dic['f1'](), dic['f2'](), dic['f3']())    #3 5 7


# 4. lambda表达式作为函数参数
def myMap(lst, value):              #序列的每一项都加value
    return map(lambda item: item + value,lst)
print(list(myMap(range(5), 3)))     #[3, 4, 5, 6, 7]

# 5. 提取大整数每位上的数字
tmp = random.randint(1,1e10)
print('tmp为:',tmp)
print(list(map(int,str(tmp))))      #[5, 5, 0, 1, 1, 9, 1, 3, 5, 2]
   

# 6. 用lambda表达式创建一个求元素个数的匿名函数
element_count = lambda lst : len(lst)
print(element_count(range(5)))

'''
    注意：在使用lambda表达式时，要注意变量作用域可能会带来的问题
'''
# 7. 变量作用域问题解析
r = []
for x in range(5):
    r.append(lambda: x**2)   #列表r追加元素
 
print(r)
print(x)
print(r[0]())       #16
print(r[1]())       #16
print(r[2]())       #16
print(r[3]())       #16

'''
    为什么无论r的下标取多少，结果都是16(4**2)呢？
    原因在lambda表达式写的有问题，这儿涉及到变量作用域的问题！
    首先要知道：这是一个嵌套函数，for循环里嵌套了lambda表达式，for循环为外部函数，lambda为内部函数。
    最关键的点：函数内部可以读取该函数外部的变量，但函数外部无法读取该函数内部定义的变量
    其次要明白r到底在内存中存储的是什么，这是打印的r：
    [
        <function <lambda> at 0x000001660F848AE8>, 
        <function <lambda> at 0x000001660F848B70>, 
        <function <lambda> at 0x000001660F848BF8>, 
        <function <lambda> at 0x000001660F848C80>, 
        <function <lambda> at 0x000001660F848D08>
    ]
    由结果可见，r的元素都是lambda表达式组成的，存储的是一组内部函数，当执行r[0]()，会执行'<function <lambda> at 0x000001660F848AE8>'
    这个函数,即lambda:x**2，因此x的值就决定了最后的输出结果。
    因为x是在for循环(外部函数)里定义的，当for循环都执行完或，x的值为4。
    当执行`r[0]()`时，首先会寻找内部函数自身(即lambda表达式)是否定义了x变量，没有则向上一层(for循环)找。
    for循环里定义了变量x，当for循环全部执行完后，x=4。此时找到了x变量，就停止寻找，返回x
    所以`r[0]()`、`r[1]()`、`r[2]()`、`r[3]()`......的值都是16。

    那如何修复这个问题？
    执行`r[0]()`时，让在内部函数自身(即lambda表达式)找到属于自己的变量就OK！
    所以做以下改造：
'''
tmp = []
for y in range(10):
    tmp.append(lambda n = y: n**2)
print(tmp[0](2))     #4     2**2
print(tmp[0](10))    #100     10**10

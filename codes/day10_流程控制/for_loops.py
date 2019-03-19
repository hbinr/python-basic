'''
流程控制--for循环
只要条件满足，就不断循环，条件不满足时退出循环。主要用于遍历/循环 序列或者集合、字典
一、for else
for target_list in expression_list:  #这个语法类似Java里的foreach循环
    pass
else:   #不满足循环条件执行，推荐不要加else
    pass
    
二、for range  else
for target_list in range(something): #这个语法类似Java里的for(int i=0;i < x; i++)
    pass
else:   #不满足循环条件执行，推荐不要加else
    pass
range函数语法:
range(start, end, step=1)，range会返回一个整数序列，
statr为整数序列的起始值，end为整数序列的结束值，在生成的整数序列中，不包含结束值。
step为整数序列中递增的步长，默认为1。
'''
tuple = (1,2,3,4,5)
list = [1,2,3,4,5]
set = {1,2,3,4,5}
dict = {1:"one",2:"two",3:"three"}

#遍历tuple，list和set类似
for i in tuple:
    print(i)

#遍历dict
for j in dict:
    print(dict.get(j))

#嵌套循环及break的使用
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        if y == 'orange':
            break;    #break 跳出当前循环，及for y in x这个内部循环
        print(y, end=" ")   #apple 1 2 3 fruit is gone
else:                 #测试else
    print('fruit is gone')

#创建从0-5的数字序列
r1 = range(0, 5)
for i in r1:
    print(i,end=" ")   #0 1 2 3 4
print()  #换行
#创建从10-30的数字序列
r2 = range(10, 30, 5)
for j in r2:
    print(j, end=" ")   #10 15 20 25

'''
range(0,5)生成包含0、1、2、3、4的整数序列，Python会把生成的这个整数序列用于for循环语句，循环从0到5，不包括5，步长为1，循环次数为5。
range(10,30,5)生成包含10、15、20、25的整数序列，循环从10到25，不包括30，步长为5，循环次数为4。
可以看出，当range用于for循环时，循环次数取决于range返回的整数序列的长度，每次循环的索引计数为整数序列的值。
'''
print() #换行

'''
    练习1：使用for循环求自然数的阶乘
'''
n = input("请出入一个自然数：")
n = int(n)
result = 1
for i in range(1, n+1):
    result *= i

# print("自然数"+ str(n) +"的阶乘为："+result)
print("阶乘结果为：",result)

'''
    练习2：降序打印10以内的偶数。方法不限
'''
#方法一：等差数列，公差为2
# for x in range(10,-1,-2):  #最简单方式 range(10,-1,-2)生成一个等差数列，公差为2，注意序列的结束值为-1，因为不包含改结束值。降序打印用负数即可
#     print(x)
#方法二：判断偶数
for x in range(10,-1,-1):    #如果start > end，步长一定要写为负数，不写是无结果的，因为默认为 正数1
    if x % 2 == 0:
        print(x)


print(range(10,20))          #range(10,20)  其返回值不再是10，11，12，13......19 了，而是range(10,20)。应该python3版本后修改了
'''
    练习3： 间隔取值--已知a列表，打印[1，4，7，10]。重点：切片的使用
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#方法一：for循环
for i in range(0, len(a), 3):
    print(a[i])
#方法二：切片的使用
b = a[0:len(a):3]     #arg1:索引起始位置， arg2:索引结束位置(不包含)， arg3: 步长
print(b)




'''
    练习4:质数算法判断
    for...else学习：else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
'''

for n in range(2,100):
    if n == 2:
        print(n)
        continue    #中途从break跳出，则连else一起跳出
    for i in range(2,int(n**0.5)+1):
        if (n%i) == 0:
            break   #中途从break跳出，则连else一起跳出
    else:
        print(n)


#也可以封装成一个函数
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2,int(n ** 0.5) + 1):
        if (n % m == 0):
            return False
    else:
        return True


for param in range(0,10):
    if is_prime(param):
        print("质数：",param)
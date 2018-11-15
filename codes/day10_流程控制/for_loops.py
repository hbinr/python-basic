'''
流程控制--for循环
只要条件满足，就不断循环，条件不满足时退出循环。主要用于遍历/循环 序列或者集合、字典
一、for else
for target_list in expression_list:
    pass
else:   #推荐不要加else
    pass
    
二、for range
for target_list in range(something):
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

#创建从0-5的数字序列
r1 = range(0,5)
for i in r1:
    print(i,end=" ")   #0 1 2 3 4
print()  #换行
#创建从10-30的数字序列
r2 = range(10,30,5)
for j in r2:
    print(j,end=" ")   #10 15 20 25

'''
range(0,5)生成包含0、1、2、3、4的整数序列，Python会把生成的这个整数序列用于for循环语句，循环从0到5，不包括5，步长为1，循环次数为5。
range(10,30,5)生成包含10、15、20、25的整数序列，循环从10到25，不包括30，步长为5，循环次数为4。
可以看出，当range用于for循环时，循环次数取决于range返回的整数序列的长度，每次循环的索引计数为整数序列的值。
'''

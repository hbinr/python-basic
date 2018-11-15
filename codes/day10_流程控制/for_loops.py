'''
流程控制--for循环
只要条件满足，就不断循环，条件不满足时退出循环。主要用于遍历/循环 序列或者集合、字典
一、for else
for target_list in expression_list:
    pass
else:   #推荐不要加else
    pass
    
一、for range
for target_list in range(something):
    pass
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
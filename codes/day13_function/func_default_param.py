'''
    默认参数：在定义函数的时候，就已经给参数复制，当调用的时候，如果没有对应的实参，那么就取默认参数的值
    但是需要注意以下事项：
    1、默认参数不允许和形参混合定义，默认参数清一色放在最后
    2、实参传入时，可以使用关键字参数来进行赋值
    3、调用函数时，给默认参数传值不允许和实参混合传值，默认参数的值清一色放在最后
'''
#练习1：定一个带有默认参数的func
def print_student_info(name, age=18, gender='男'):
    print("我叫：" + name)
    print("年龄：" + str(age))
    print("性别：" + gender)

#不允许混合顺序定义
# def error_demo(name,age=18,gender):    #non-default parameter follows default parameter
#语法错误  非默认参数放在了默认参数后面，不允许
#1、正常传实参调用
print_student_info("大熊",13,'男')
# 我叫：大熊
# 年龄：13
# 性别：男

#2、使用默认参数
print_student_info("小彬")
# 我叫：小彬
# 年龄：18
# 性别：男

print_student_info("大彬",20)
# 我叫：大彬
# 年龄：20
# 性别：男


#3、关键字参数，入参顺序和函数定义的参数顺序无关

print_student_info("小蕾",gender='女',age=20)
# 我叫：小蕾
# 年龄：20
# 性别：女

#4、混合入参  不允许
# print_student_info("小蕾",age=20,'女')    #SyntaxError: positional argument follows keyword argument
#报语法错误 位置参数放在了关键字参数后面,不允许
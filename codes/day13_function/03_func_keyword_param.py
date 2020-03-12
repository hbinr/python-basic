"""
    关键字参数：用于函数调用，通过“键-值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
    
    注意：有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序的
"""


# 定一个普通函数

def print_student_info(name, age, gender):
    print("我叫：" + name)
    print("年龄：" + str(age))
    print("性别：" + gender)


# 以下是正确的调用实例
print_student_info("大熊", age=1, gender='男')
print_student_info("大熊", 18, gender='男')
print_student_info(name="大熊", age=18, gender='男')
print_student_info(age=19, name="大熊", gender='男')  # 参数顺序修改

# 以下是错误确的调用实例，位置参数必须在关键字参数的前面

# print_student_info(name="大熊", 18, gender='男')    #报错
# print_student_info("大熊", age=18, '男')            #报错

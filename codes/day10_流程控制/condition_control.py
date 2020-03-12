'''
流程控制--条件控制
1、if else
if condition:
    pass
else:
    pass
2、if elif else ,elif是与if配对出现的
if condition1:
    pass
elif condition2:
    pass
else:
    pass
3、python中没有switch
   可以使用字典方式来代替
'''

print("请输入1、2、3中的任意值")
a = input()
# a = int(a)
if a == 1:
    print("输入值为 1")
elif a == 2:
    print("输入值为 2")
elif a == 3:
    print("输入值为 3")
else:
    print("非法输入！")

# 在实际操作中，从命令行接收的值都为str类型，所以上述代码无论输入什么值都是返回 "非法输入!"。所以需要将str转为int，调用int()即可

'''
    利用字典实现switch
'''


def taskForSunday():
    print("今天休息")


def taskForRest():
    print("今天休息")


def taskForChinese():
    print("今天上语文课")


def taskForMath():
    print("今天上数学课")


def taskForEnglish():
    print("今天上英语课")


def taskForDefault():
    print("输入错误。。。。")


switchDic = {"Sunday": taskForRest,
             "Monday": taskForChinese,
             "Tuesday": taskForMath,
             "Wednesday": taskForEnglish,
             "Tursday": taskForEnglish,
             "Friday": taskForEnglish,
             "Saturday": taskForRest
             }

switchDic.get("Sunday", taskForDefault)()  # 今天休息
switchDic.get(213, taskForDefault)()  # 输入错误。。。。 测试时，每次都得写.get(xx,taskForDefault)()，所以优化一下


# 优化后
def switchDicNew(var):
    return {
        "Sunday": taskForRest,
        "Monday": taskForChinese,
        "Tuesday": taskForMath,
        "Wednesday": taskForEnglish,
        "Tursday": taskForEnglish,
        "Friday": taskForEnglish,
        "Saturday": taskForRest
    }.get(var, taskForDefault)()


switchDicNew("Friday")

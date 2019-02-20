'''
    Enum 在Python,其本质就是一个Class,使用枚举可以帮助我们更好的知道自己想要的类型,比如：一月：1、二月:2
    通过code值来唯一标识自定义类型，而不用去关注code编码到底是多少
    通过导入Enum包来引入枚举类,定义的时候直接继承Enum即可
    个人经验：
        Java 在实际开发中,code编码如何涉及到跨服务调用,一定要和对接人联系好对方是用什么类型接受该code值,
    是纯数字还是字母和数字组合? 否则会出现数据流不一致,调接口报错
        但是在Python中不会有上述问题,Python是动态语言,会自动转换类型
'''
from enum import Enum


#定义月份枚举
class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


#打印Month类
print(Month)     #<enum 'Month'>   Month类是枚举类

# 类名.属性 会直接输出1吗？
print(Month.JANUARY)    #Month.JANUARY   如果是普通的类,应该输出的结果是1，但此处调用却输出了枚举值

#取标签具体值
print(Month.JANUARY.name)    #JANUARY

#取枚举值
print(Month.JANUARY.value)

'''
    通过上述实践,Month.JANUARY和JANUARY有什么区别呢？
    
'''
#打印他们的类型
print(type(Month.JANUARY))              #<enum 'Month'>   一个是枚举

print(type(Month.JANUARY.name))         #<class 'str'>    一个是字符串

#通过名称获取枚举的类型
print(Month['JANUARY'])                 #Month.JANUARY


#遍历所有枚举类型

for v in Month:
    print(v)
'''
结果：
Month.JANUARY
Month.JANUARY
Month.FEBRUARY
Month.MARCH
Month.APRIL
Month.MAY
Month.JUNE
Month.JULY
Month.AUGUST
Month.SEPTEMBER
Month.OCTOBER
Month.NOVEMBER
Month.DECEMBER

'''

'''
    总结：
    枚举类型：Month.JANUARY
    枚举的名字：Month.JANUARY.name
    枚举值：Month.JANUARY.code
'''
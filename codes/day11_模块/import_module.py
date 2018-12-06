'''
Python中导入模快
主要包括以下几种导入方式：

1、import modules(模块名字)   #导入整个模块，这种导入方式比较占用内存

2、import modules (模块名字)  as  XX               #这里是导入整个模块的同时给它取一个别名，因为有些模块名字比较长，
                                                   用一个缩写的别名代替在下次用到它时就比较方便
3、from modules(模块名字)  import func(方法）或者变量      #从一个模块里导入方法或者变量 ，你要用到模块里的哪个方法
                                                           或者变量就从模块里导入哪个方法或者变量，这样占用的内存就比较少
也可以用别名表示 ： from modules(模块名字)  import func(方法）或者变量  as   XX

也支持from 包名 import 模块名  这种写法不太推荐，和 import modules(模块名字)一样了，既然有这个from xxx import  xxx用法，
肯定有它的用处
'''



'''
导入模块其实就是告诉Python解释器去解释那个py文件，注意：包和模块是不会被重复导入的

1、导入一个py文件，解释器解释该py文件
2、导入一个包，解释器解释该包下的 __init__.py 文件
'''
#练习1：导入 day04_listAndTuple包下的list.py模块

import codes.day04_listAndTuple.list as ls           #导入list模块
from codes.day05_set.set import set1 as set         #导入set模块下的set1变量
from codes.day06_dict.dict import *                 #导入dict模块下__all__列表里的变量，也就是说，以*导入时，package内
                                                    #的module是受__init__.py限制的。
from codes.day06_dict.dict import list,tuple,set,\
    dict                                            #但是python不建议使用import *来导入，如果需要导入多个变量，可以用逗号分隔，
                                                    #用反斜杠'\'来换行  也不推荐 。。使用()来包裹要导入的变量即可:
                                                    #(list,tuple,set,dict)


print("import_module开始调用list模块里list变量，结果为：")
test = ls.list
print(test[0:])   #['2', 2.5, 'Hello', True, 7j]

#事实上，导入list模块后，会把改模块下面所有内容都导过来，在执行本程序时(import_module)时，原list模块的内容会原封不动的先输出，
# 然后才是本模块的内容输出，因为python解释器是按照顺序来执行的。(先定义后使用)

print("import_module开始调用set模块里set1变量，结果为：")
print(set)        #{2, 3, 4, 5, 'Hello', 7}  在导入dict模块后值变为{1, 2, 3}了，因为变量名重名，后导入的模块将前面导入的变量给覆盖掉了
# print("import_module开始调用dict模块里的内置变量，结果为：",*)   #这种写法是不正确的，虽然使用了 * 符号，但是不能在使用它作为导入的变量来直接使用

#应该为：  __all__ = ["list","tuple","set","dict"]
print("import_module开始调用dict模块里的内置变量list，结果为：",list)      #[1, 2, True]
print("import_module开始调用dict模块里的内置变量tuple，结果为：",tuple)    #(1, 'hello', 'world', 72j)
print("import_module开始调用dict模块里的内置变量set，结果为：",set)        #{1, 2, 3}
print("import_module开始调用dict模块里的内置变量dict，结果为：",dict)      #{1: 'one', 2: 200, '404': 'Not found'}
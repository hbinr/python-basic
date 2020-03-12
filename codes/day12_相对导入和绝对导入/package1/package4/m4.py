from .m4_1 import temp4_1
from ..m1 import temp1

'''
相对导入练习：
先梳理下思路：
    第一步：在day12_相对导入和绝对导入/main.py入口文件中绝对导入了 m4模块，执行的代码是:import  package1.package4.m4
    第二步：然后在m4中相对导入了同级m4_1模块和上一级的m1模块
    第三步：运行main.py入口文件，查看结果
'''
temp4 = 4
print('m4模块的__package__为：', __package__)  # m4模块的__package__为： package1.package4

print('m4_1模块的变量temp4_1的值为：', temp4_1)  # m4_1模块的变量temp4_1的值为： 41

print('m1模块的变量temp1的值为：', temp1)  # m1模块的变量temp1的值为： 1

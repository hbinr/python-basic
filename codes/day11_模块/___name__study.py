'''
    记录__name__的经典应用
    通过Python程序的__name__属性可以识别程序的使用方式，每个Python脚本在运行时都会有一个__name属性，如果脚本作为模块被
    导入，则其__name__属性的值被自动设置为模块名；如果脚本作为程序直接运行，则其__name__属性值则被自动设置为字符串
    '__main__'。
    常用来判断某python是被用作一个入口执行文(或称为脚本)件还是用作一个普通模块

'''

if __name__ == '__main__':    #选择结构，识别当前的运行方式
    print('This program is run directly.')
else:
    print('This progtam is used as a module.')
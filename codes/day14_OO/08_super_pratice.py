"""
    Python 关于super 的 用法和原理
    摘自:https://www.cnblogs.com/xinghuaikang/p/8481712.html
"""


class A():
    def go(self):
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")


class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class D(B, C):
    def go(self):
        super(D, self).go()
        print("go D go!")

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")


class E(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
e = E()

a.go()
print('--------')
b.go()
print('--------')
c.go()
print('--------')
d.go()
print('--------')
e.go()

# 多重继承，类的顺序
print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>]

# print('--------')
# a.stop()
# print('--------')
# b.stop()
# print('--------')
# c.stop()
# print('--------')
# d.stop()
# print('--------')
# e.stop()

# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()

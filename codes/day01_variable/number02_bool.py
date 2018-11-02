#bool类型可以划分number范畴  因为在Python中,非0为true,0为False
print(type(True)) #<class 'bool'>
print(bool)   #<class 'bool'>

print(int(True))  #1  bool转为十进制表示1或0

print(bool(1)) #True
print(bool(1.2)) #True
print(bool(-1.2)) #True
print(bool(0b10)) #True

print(bool(0)) #False

#但是并不是只有数字才能表示bool, 传入元组、列表、字典等对象时，元素个数为空返回False，否则返回True
print(bool())  #False  bool函数入参为空,表示为False
#字符串  空字符串返回False，否则返回True
print(bool("Hello world")) #True
print(bool("")) #False
#元组
print(bool((1,2,3))) #True
print(bool(())) #False
#列表
print(bool([1,2])) #True
print(bool([])) #False
#字典
print(bool({1,2,3})) #True
print(bool({})) #False

#None
print(bool(None)) #False
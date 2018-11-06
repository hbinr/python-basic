# binary 二进制的  0 1 那么2表示10
# octal 八进制的  0,1,2,3,4,5,6,7  那么8表示为10
# hexadecimal 十六进制的  0,1,2,3.....9,A,B,C,D,E,F
# decimal 十进制的 0,1,2,3,4,5,6,7,8,9,10

# BIN、OCT、HEX、DEC分别代表二、八、十六、十进制~

#二进制
print(0b10)  #2
#八进制
print(0o10)  #8
#十进制
print(10)    #10
#十六进制
print(0xA)   #10
print(0xB)   #11
print(0xF)   #15
print(0x10)  #16


#将其他进制转为二进制  bin()
print("将十进制转为二进制:"+bin(2))  # 0b10   即2
print("将八进制转为二进制:"+bin(0o10))  # 0b1000 即8
print("将十六进制转为二进制:"+bin(0x10))  # 0b10000 即16

print("bin(2)二进制是以str类型存储的:" + bin(2))  #str   二进制数是字符串类型

#将其他进制转为八进制  oct()
print("将十进制转为八进制:"+oct(2))  # 0b10   即2
print("将八进制转为八进制:"+oct(0o10))  # 0b1000 即8
print("将十六进制转为八进制:"+oct(0x10))  # 0b10000 即16

print("oct(2)二进制是以str类型存储的:" + oct(2))  #0o2   八进制数是字符串类型

#将其他进制转为十进制  int()
# print("将二进制转为十进制:"+int(0b10))  # 2 这行代码会报错，因为十进制数在python是以int型存储的,TypeError: can only concatenate str (not "int") to str

print(int(0b10))  # 2  将二进制转为十进制
print(int(0o10))  # 8  将八进制转为十进制
print(int(0x10))  # 16 将十六进制转为十进制

#将其他进制转为十六进制  hex()
print("将十进制转为十六进制:"+hex(2))  # 0b10   即2
print("将八进制转为十六进制:"+hex(0o10))  # 0b1000 即8
print("将十六进制转为十六进制:"+hex(0x10))  # 0b10000 即16

print("hex(2)十六进制是以str存储的:" + hex(10))  #0xa  十六进制数是字符串类型



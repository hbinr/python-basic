1  # 整数  int
1.2222  # 浮点数 float-双精度  没有double

# 打印以下数据类型
print(type(1 + 0.1))  # 1.1 float
print(type(1 + 1))  # 2 int
print(type(1 + 1.0))  # 2.0 float

print(type(1 * 1.0))  # 1.0 float
print(type(1 * 1))  # 1 int
print(type(2 / 2))  # 1.0 float---- 两个整数相除，特别注意，一个单斜杠得到float，自动转为浮点数
print(type(2 // 2))  # 1 int---- 特别注意，两个个单斜杠得到int，自动取整，即整除概念
print(type(1 // 2))  # 0 int
print(type(1 + 1.0))  # 2.0 float

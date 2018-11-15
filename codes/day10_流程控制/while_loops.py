'''
流程控制--while循环
只要条件满足，就不断循环，条件不满足时退出循环。递归场景常用while循环，一般场景用for较合适
while condition:
    pass
else:
    pass
另外两个常用与循环的关键字:
break
在循环中，break语句可以提前退出循环

continue
在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
'''

#打印1~10
n = 1
while n <= 10:
    #输出的结果是列展示，如果想一行展示，需要在print()函数中加参数，print("",end = "")，是所以会列展示，是默认加的是end="/n"
    print(n,end = " ")
    n += 1
print("打印1~10结束")


#只打印5(包括5)之前的数
m = 1
while m <= 10:
    print(m,end = " ")
    m += 1
    if m > 5:
        break;
print("只打印5(包括5)之前的数结束")


#只打印10以内的奇数
q = 1
while q < 10:
    q += 1
    if q % 2 == 0:
        continue;

    print(q,end = " ")

print("除了5之外的数都打印")
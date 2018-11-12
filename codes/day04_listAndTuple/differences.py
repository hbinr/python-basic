#元组tuple和列表list最大的区别就是：tuple是不可变的，而list是可变的

#如何获取4？
test = (1,2,[2,3,4])
print(test[2])     #[2, 3, 4]
print(test[2][2])  #4

#修改元组中list的值  4->"hello"
test[2][2] = "hello"

print(test)        #(1, 2, [2, 3, 'hello'])。本质上是对list做了操作


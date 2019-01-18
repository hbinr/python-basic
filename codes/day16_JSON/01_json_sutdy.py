'''
    JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式
    优点：于人易阅读和编写。同时也易于机器解析和生成，也易于机器解析和生成，并有效地提升网络传输效率，可跨语言交换数据
    
    字符串是JSON的表现形式
    JSON字符串：符合JSON格式的字符串就是JSON字符串
'''
import json

dict_data = {"name":"RongEr","age":18,"love":"reading"}
'''
1、json.dumps  将 Python 对象编码成 JSON 字符串
'''
json_dict = json.dumps(dict_data)
print(json_dict)

'''
2、json.loads  将已编码的 JSON 字符串解码为 Python中的数据结构
   JSON结构类似Python中的dict，那么将Json字符串loads后，该数据结构是不是就是dict?
'''
json_data = '{"name":"RongEr","age":18,"love":"reading"}'
object_json = json.loads(json_data)
print(object_json)         #{'name': 'RongEr', 'age': 18, 'love': 'reading'}  注意原来的双引号都变为单引号了，因为在python中，
                           # dict的底层定义默认是单引号
print(type(object_json))   #<class 'dict'>，经验证，该数据结构本质上是一个dict



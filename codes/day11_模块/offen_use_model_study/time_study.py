#!/usr/bin/python

# -*- coding: utf-8 -*-

'''
    time时间模块的学习
        时间元组（年、月、日、时、分、秒、一周的第几日、一年的第几日、夏令时）
        一周的第几日: 0-6
        一年的第几日: 1-366
        夏令时: -1, 0, 1 (默认为-1)
    
'''
import time

# 1. time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
print('time()当前时间戳：',time.time())   #time()当前时间戳： 1557328843.3729122

# 2. localtime([secs])  接收时间戳并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）
localtime_one = time.localtime(time.time())
print('localtime([secs]):',localtime_one)
print('localtime()的返回值类型为:', type(localtime_one))   #localtime()的返回值类型为: <class 'time.struct_time'> time视图
'''
输出结果为：
time.struct_time(tm_year=2019, tm_mon=5, tm_mday=8, tm_hour=23, tm_min=20, tm_sec=43, tm_wday=2, tm_yday=128, tm_isdst=0)
'''

# 3. asctime([tupletime]) 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）
#                         的24个字符的字符串。
localtime_two = time.asctime( time.localtime(time.time()) )
print('asctime(arg),本地时间为：',localtime_two)       #asctime(arg),本地时间为： Wed May  8 23:25:42 2019
print('asctime()无参的结果为:',time.asctime())     #asctime()无参的结果为: Wed May  8 23:25:42 2019

# 4. ctime([secs])  作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print('ctime():',time.ctime())             #ctime(): Wed May  8 23:20:43 2019

# 5. sleep(secs) 推迟调用线程的运行，secs指秒数。
for x in range(5):
    time.sleep(1)  #推迟1s
    print(x)


# 6. strftime()   时间元组 → 可视化时间（定制）(要转换成的格式，时间元组)
strftime_tmp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print('strftime()格式化时间:',strftime_tmp)     #strftime()格式化时间: 2019-05-08 23:34:22

"""
    python中时间日期格式化符号：
    ------------------------------------
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称  # 乱码
    %% %号本身
"""
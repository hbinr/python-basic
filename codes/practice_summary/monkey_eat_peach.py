#!/usr/bin/python 

# -*- coding: utf-8 -*-

# 猴子吃桃问题
# 猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个,
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少?

# 分析:第10天i个，第九天(i+1)*2个......以此类推，逆向考虑，逻辑比较简单
peachnum_first_day = 1  #第一天的桃子数
for i in range(9):      #处理剩下9天的
    peachnum_first_day = peachnum_first_day*2 + 2
print('第一天的桃子数为:',peachnum_first_day)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑
多加一天：
程序源代码：'''

years= int(input('input years :'))
mounths = int(input('input mounths:'))
days = int(input('input days :'))
mounth_day = 0
mounth_run=[31,29,31,30,31,30,31,31,30,31,30,31]
mounth_ping=[31,28,31,30,31,30,31,31,30,31,30,31]

if years%100==0 or years%4==0 :
    for i in range(mounths-1):
        mounth_day+=mounth_run[i]
    all_day = mounth_day+days
    print all_day
else:
    for i in range(mounths-1):
        mounth_day+=mounth_ping[i]
    all_day =mounth_day+days
    print  all_day

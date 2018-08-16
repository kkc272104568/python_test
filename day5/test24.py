#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。

程序源代码：
'''


def total (n):
    x1=1.0
    x2=2.0
    s=x2/x1
    for i in range (n-1):
        temp =x2
        x2=x1+x2
        x1 = temp
        s=s+x2/x1
    print s
total(20)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无。

程序源代码：
'''

i=input('input a number :')
k=0
while k==0:
    k1 = (i / 1) % 10
    k2 = (i / 10) % 10
    k3 = (i / 100) % 10
    k4 = (i / 1000) % 10
    k5 = (i / 10000) % 10
    if (k1==k5)and (k2==k4):
        print 'i是回文数'
        k=1
    else:
        i=input('请重新输入 input a number :')

#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。

程序源代码：
'''
i=input('input a number :')
k=0
if  i>0 and i<100000:
    if (i /10000)>0:
        print 'i 为五位数'
        k=5
    elif (i/1000)>0:
        print 'i 为四位数'
        k=4
    elif (i /100)>0:
        print 'i 为三位数'
        k=3
    elif (i/10)>0:
        print 'i 为两位数'
        k=2
    elif (i)>0:
        print 'i 为个位数'
        k=1
else:
    print 'please input again :'
w=1
for s in range(k):
    k1=(i/w)%10
    w=w*10
    print k1

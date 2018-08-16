#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。
'''

def sum(n):
    w=0
    all=0
    for i in range (1,n+1):
        s=1
        for j in range(1,i+1):
            s=s*j
        w =s
        print 'w',w
        all =all+w
    print 'all',all

sum(20)
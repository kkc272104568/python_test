#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：两个变量值互换。

程序分析：无

程序源代码：
'''

def change(a,b):
    temp=a
    a=b
    b=temp
    return a,b
print change(4,3)

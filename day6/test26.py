#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!

程序源代码：
'''

def dd(n):
    s= 1
    for i in range(1,n+1):
        s= s*i
    print s

dd(5)
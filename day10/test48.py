#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：数字比较。

程序分析：无

程序源代码：
'''

def compare(a,b):
    if a>b:
        print  '%d大于%d'%(a,b)
    elif a== b:
        print  "%d等于%d"%(a,b)
    else:
        print  "%d小于%d"%(a,b)

compare(1,3)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：
0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：
'''

def F(x):
    if x==0 :
        return 0
    elif x==1 :
        return 1
    else:
        result= F(x-1)+F(x-2)
        return result

print F(15)


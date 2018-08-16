#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。

程序源代码：
'''

a=[1,2,3,7,10]
print a
x= len(a)
for i in (range(x/2)):
    a[i], a[x - i - 1] = a[ x- i - 1], a[i]
print a
#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：按逗号分隔列表。

程序分析：无。
'''
L = [1, 2, 3, 4, 5]
L = repr(L)[1:-1]
print L

l = [1,2,3,4,5,6,7]
o = ''
for i in l:
    o += str(i)+','
print(o[0:-1])
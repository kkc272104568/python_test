#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

程序分析：无。
'''
for i in range(7):
    x=int(raw_input('please input a number :\n'))
    for w in range(x):
        print '*',
    print


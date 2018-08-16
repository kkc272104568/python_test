#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。

程序分析：无

程序源代码：
'''
x= input('please input a number ')
w=1
while w==1:
    if x**2>=50 :
        x=input("please input a new number ")
        w=1
    else:
        print 'the squeal of the number is small than 50 ! '
        w=0
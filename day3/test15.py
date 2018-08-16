#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

程序源代码：
'''


def degreed(x):
    if   0<=x and x<=100:
        if x>= 90 :
            print "A"
        elif  60<=x<=89:
            print "B"
        else:
            print "C"
    else:
        print "please input  correct score !"

degreed(800)
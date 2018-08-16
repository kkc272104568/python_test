#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

程序分析：无。

程序源代码：
'''


def will(n):
    if n%2==0:
        x=0.0
        w=0.0
        for i in range(n/2):
            x=x+2
            w=1/x+w
        print w
    else:
        x=-1.0
        w=0.0
        for i in range (n/2+1):
            x=x+2
            w=1/x+w
        print w
will(4)

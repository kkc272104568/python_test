#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：输入3个数a,b,c，按大小顺序输出。　　　

程序分析：无。

程序源代码：
'''

def compare(a,b,c):
    x=0
    y=0
    if a>b :
       x=a
       if x<c :
           print c,a,b
       elif x>c :
           if b>c :
               print a,b,c
           else:
               print a,c,b
    elif a<b :
        x=b
        if x<c :
            print c,b,a
        elif x>c:
            if a>c :
               print b,a,c
            else:
                print b,c,a

compare(1,9,5)
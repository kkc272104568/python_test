#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：反向输出一个链表。

程序分析：无。
'''

if __name__ =='__main__':
    str=[]
    for i in range(5):
        num= raw_input("please input a number :\n")
        str.append(num)
    str.reverse()
    print str
#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：八进制转换为十进制

程序分析：无
'''
def change(n):
    w=0
    l=str(n)
    for i in range(len(l)):
        w=8**i*int(l[len(l)-i-1])+w
    print w

change(122)

# def f8to10(num):
#     print("8进制数：", num)
#     l = str(num)
#     length = len(l)
#     sum = 0
#     for i in range(length):
#         sum += 8 ** i * int(l[length-1-i])
#     print("转成10进制数为：",sum)
#
# f8to10(122)
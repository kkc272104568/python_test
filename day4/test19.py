#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

程序分析：请参照程序Python 练习实例14。

程序源代码：
'''
# nums =int(input('please in put a number :'))
# # t= range(nums)
# # print t]
# s=[]
# while nums!=1:
#     for i in range(2,nums+1):
#         if nums%i==0:
#            s.append(i)
#            nums=nums/i
#            break
# print s
# import numpy as np
#
# for numss in range (2,1001):
#     num=numss
#     resoult=0
#     s = [1]
#     w = []
#     while num != 1:
#         for i in range(2, num + 1):
#             if num % i == 0:
#                 s.append(i)
#                 num = num/ i
#                 break
#     if numss== np.sum(s):
#         print numss

import numpy as np

for m in range(1,1001):
    n=[1]
    for i in range(2,m):
        if m % i == 0:
            n.append(i)
    if m == np.sum(n):
        print m,n

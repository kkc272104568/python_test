#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：求100之内的素数。

程序分析：无。

程序源代码：
'''

x=[]
# w=[]
# for y in range(1,101):
#     w.append(y)
# print w
# for i in range (2,101):
#     for j in range (2,i):
#         if (i%j)==0 :
#             break
#         else:
#             print i


for num in range(1,101):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
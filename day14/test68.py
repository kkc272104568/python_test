#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

程序分析：无。

程序源代码：
'''

from collections import deque

m = 3
a = [1,2,3,4,5,6,7]   # 7 个数
f = deque(a)
f.rotate(m)
print list(f)


######方法2
m = 3
a = [1,2,3,4,5,6,7]

def rot(a,n):
    l = len(a)
    n = l-n
    return a[n:l]+a[0:n]

b = rot(a,m)

print a
print b
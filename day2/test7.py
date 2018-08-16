#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。

程序源代码：'''

a = [1, 2, 3]
b=[]
for i in range(len(a)):
    b.append(a[i])
print b
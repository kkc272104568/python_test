#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

程序源代码：'''

str = [1,2,3,4,5,6,7,8,9]

for i in str:
    print
    for j in str :
        if j <= i :
            print"%d*%d=%d" % (i, j, i*j),
#
# for i in range(1, 10):
#     print
#     for j in range(1, i+1):
#         print "%d*%d=%d" % (i, j, i*j),
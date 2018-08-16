#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：打印出杨辉三角形（要求打印出10行如下图）。　　

程序分析：无。

程序源代码：
'''

def yanghui(n):
    x=[]
    for i in range(n):
        x.append([])
        # print x
        for j in range(n):
            x[i].append(1)
    # print x
    for i in range(2,10):
        for j in range(1,i):
            x[i][j] = x[i - 1][j - 1] + x[i - 1][j]
    print x
    # from sys import stdout
    # for i in range(10):
    #     for j in range(i + 1):
    #         stdout.write(str(x[i][j]))
    #         stdout.write(' ')
    #     print
    w=[]
    for i in range (10):
        w.append([])
        for j in range (i):
            w[i].append[x[i][j]]
    print w
yanghui(10)

# if __name__ == '__main__':
#     a = []
#     for i in range(10):                 #编译出a[][] ，且所有的值均为0
#         a.append([])
#         for j in range(10):
#             a[i].append(0)
#     print a
#     for i in range(10):
#         a[i][0] = 1             #g固定首位均为1
#         a[i][i] = 1
#     for i in range(2,10):
#         for j in range(1,i):
#             a[i][j] = a[i - 1][j-1] + a[i - 1][j]
#             print a[i][j]
#     from sys import stdout
#     for i in range(10):
#         for j in range(i + 1):
#             stdout.write(str(a[i][j]))
#             stdout.write(' ')
#         print
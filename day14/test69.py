#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

程序分析：无。

程序源代码：
'''
def rotate() :
    if __name__ == '__main__':
        nmax = 50       #设定最大值
        n = int(raw_input('请输入总人数:'))   #设定输入人数
        num = []                                #设定一个数组用于接收数值
        for i in range(n):
            num.append(i + 1)

        i = 0
        k = 0
        m = 0

        while m < n - 1:
            if num[i] != 0: k += 1
            if k == 3:
                num[i] = 0
                k = 0
                m += 1
            i += 1
            if i == n: i = 0

        i = 0
        while num[i] == 0: i += 1
        print num[i]
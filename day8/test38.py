#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：求一个3*3矩阵主对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。

程序源代码：
'''
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
w = 0
for i in range(a.shape[1]):
    w=a[i][i]+w
print w




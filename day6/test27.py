#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

程序分析：无。

程序源代码：'''


sting= raw_input('please input 5 string:')
x=len(sting)
w=[]
for i in range(x):
    w.append(sting[x-i-1])
print w
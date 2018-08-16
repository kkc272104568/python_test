#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

程序分析：无

程序源代码：'''

def high(x,n):
    s= float(x)
    re=s
    for i in range(n-1) :
        s=s/2
        re=re+s*2
    print float(re),s/2

high(100,10)
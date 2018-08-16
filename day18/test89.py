#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

程序分析：无。

程序源代码：
'''
def jiami():
    w=str(raw_input('please input you number :\n'))
    print w[1]
    s=[]
    for i in range (len(w)):
        s.append((int(w[i])+5)%10)
    print s
    for i in range(len(s)/2):
        s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
    print s

jiami()
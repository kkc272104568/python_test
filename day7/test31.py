#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

程序源代码：
'''
x= raw_input('please input the first alapha:')
print x
w=1
while w==1:
    if x =='M'or x=='m':
        print 'today is Monday'
        w=0
    elif x== 'W'or x== 'w':
        print 'today is Wednesday'
        w=0
    elif x=='F'or x== 'f':
        print 'today is friday'
        w=0
    elif x=='T'or x== 't':
        y= input("please input the second alapha")
        if y == 'u'or y=='U':
            print  'today is Tuesday'
            w=0
        elif y=='h'or y=='H':
            print 'today is Thursday'
            w=0
        else:
            print ' input error  !'
            w=1
    elif x == 'S' or x == 's':
        y = input("please input the second alapha")
        if y == 'a' or y == 'A':
            print  'today is Saturday'
            w=0
        elif y == 'u' or y == 'U':
            print 'today is Sunday'
            w=0
        else:
            print ' input error !'
            w=1
    else :
        x= raw_input('input error ,please reinput :')

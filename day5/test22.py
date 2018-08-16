#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，
请编程序找出三队赛手的名单。

程序源代码：
'''

jia = ['a','b','c']
yi = []

for  i in  range(3):
    if jia[i]!='a' and jia[i]!= 'c':
       yi.insert(i,'x')
    elif jia[i]!='c':
       yi.insert(i,'z')
    else:
       yi.insert(i,'y')

print yi
#
# 方法2 ：
for a in ['x','y','z']:
    for b in ['x', 'y', 'z']:
        for c in ['x', 'y', 'z']:
            if(a!=b)and(b!=c)and(c!=a) and (a!='x') and (c!='x') and (c!='z'):
                print 'a和%s比赛，b和%s比赛，c和%s比赛' %(a,b,c)
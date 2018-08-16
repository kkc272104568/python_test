#!/usr/bin/python
# -*- coding: UTF-8 -*-\

'''
题目：列表排序及连接。

程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。

程序源代码：
'''


if __name__=="__main__":
    str1=[1,3,2,7,6,5]
    str2=[3,3,3]
    str1.sort()
    print str1
    str3=str1+str2
    str1.extend(str2)
    print str3
    print str1
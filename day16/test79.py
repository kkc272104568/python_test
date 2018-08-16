#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：字符串排序。

程序分析：无。
'''
if __name__ == "__main__":
    ls =[]
    str1 = raw_input('请输入第一个字符串：')
    str2 = raw_input('请输入第二个字符串：')
    str3 = raw_input('请输入第三个字符串：')
    ls.extend([str1,str2,str3])
    ls.sort()
    print ls


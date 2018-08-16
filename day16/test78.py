#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：找到年龄最大的人，并输出。请找出程序中有什么问题。

程序分析：无。

程序源代码：
'''

if __name__ == '__main__':
    person = {"li": 18, "wang": 20, "zhang": 50, "sun": 22}
    m = 'li'
    for key in person.keys():
        print person[key]
        if person[m] < person[key]:
            m = key

    print '%s,%d' % (m, person[m])
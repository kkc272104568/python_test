#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：使用lambda来创建匿名函数。
 def func(x):
    return(x+1)
可以这样认为,lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体。
在这里lambda简化了函数定义的书写形式。是代码更为简洁，但是使用函数的定义方式更为直观，易理解。
程序分析：无
'''

MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print 'The largar one is %d' % MAXIMUM(a, b)
    print 'The lower one is %d' % MINIMUM(a, b)
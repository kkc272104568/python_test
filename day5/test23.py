#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''题目：打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *
'''

from sys import stdout

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print

# 方法2
for i in range(4):
    print((3-i)*' '+(2*i+1)*'*')
for i in range(3):
    print((i+1)*' '+(5-2*i)*'*')
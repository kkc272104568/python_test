#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''题目：输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
如果x>z则将x与z的值进行交换，这样能使x最小。

程序源代码：'''

x= int(input('输入第一个整数 :'))
y = int(input('输入第二个整数:'))
z= int(input('输入第三个整数 :'))

if x > y :
    max = x
    temp1= y
    if max> z :
        temp2 =z
        if temp1>temp2 :
            print max,temp1,temp2
        else:
            print max,temp2,temp1
    else:
        temp2 = max
        max = z
        if temp1 > temp2:
            print max, temp1, temp2
        else:
            print max, temp2, temp1
else:
    max = y
    temp1= x
    if max> z :
        temp2 =z
        if temp1>temp2 :
            print max,temp1,temp2
        else:
            print max,temp2,temp1
    else:
        temp2 = max
        max = z
        if temp1 > temp2:
            print max, temp1, temp2
        else:
            print max, temp2, temp1

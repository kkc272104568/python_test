#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：画图，学用line画直线。

程序分析：无。
'''

from Tkinter import *
canvas=Canvas(width=300,height=300,bg='white')
canvas.pack(expand=YES, fill=BOTH)
x1,y1=50,20
x2,y2=100,20
x3,y3=75,40
x4,y4=75,100
canvas.create_line(x1,y1,x3,y3, width=3, fill='red')
canvas.create_line(x2,y2,x3,y3, width=3, fill='red')
canvas.create_line(x1,y1,x4,y4, width=3, fill='red')
canvas.create_line(x2,y2,x4,y4, width=3, fill='red')
mainloop()
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# if __name__ == '__main__':
#     from Tkinter import *
#
#     canvas = Canvas(width=800, height=600, bg='yellow')
#     canvas.pack(expand=YES, fill=BOTH)
#     k = 1
#     j = 1
#     for i in range(0, 26):
#         canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
#         k += j
#         j += 0.3
#
#     mainloop()

# if __name__ == '__main__':
#     import turtle
#     turtle.title("画圆")
#     turtle.setup(800,600,0,0)
#     pen=turtle.Turtle()
#     pen.color("yellow")
#     pen.width(5)
#     pen.shape("turtle")
#     pen.speed(1)
#     pen.circle(100)

import numpy as np
import matplotlib.pyplot as plt

x = y = np.arange(-11, 11, 0.1)
x, y = np.meshgrid(x,y)
#圆心为（0，0），半径为1-10
for i in range(1,11):
   plt.contour(x, y, x**2 + y**2, [i**2])
   #如果删除下句，得出的图形为椭圆
   plt.axis('scaled')
plt.show()

# import math as m
# import matplotlib.pyplot as plt
#
# x=[]
# y=[]
# for a in range(1,11):
#     for b in range(0,360):
#         x.append(a*(m.cos(m.pi*(b/180))))
#         y.append(a*(m.sin(m.pi*(b/180))))
# plt.scatter(x,y,s=30)
# plt.axis([-11,11,-11,11])
# #避免因比例而压缩为椭圆
# plt.axis('equal')
# plt.show()


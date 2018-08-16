#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。

程序源代码：'''

a=input('输入要相加的数是:')
n=input('相加的数个数为：')
s=a
end=0
for i in  range(n) :
    a=a*10+s
    print a
    end =end +a
print end

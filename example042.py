#/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
题目描述：函数本地变量的使用
"""

#原始程序
num = 2
def autofunc():
    num = 1 #函数本地变量在函数调用结束后消失
    print('internal block num = %d' % num)
    num += 1
for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()
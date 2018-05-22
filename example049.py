#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example049.py
#Author: kernellmd 
#Created Time: 2018-05-22 19:14:25
############################  

"""
题目描述：数字比较
"""

#原始程序
if __name__ == '__main__':
    i = int(input("x:"))
    j = int(input("y:"))
    if i > j:
        print('%d > %d' % (i,j))
    elif i == j:
        print(' %d == %d' % (i,j))
    else:
        print('%d < %d' % (i,j))

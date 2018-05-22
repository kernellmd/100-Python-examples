#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example048.py
#Author: kernellmd 
#Created Time: 2018-05-22 19:10:39
############################  

"""
题目描述：使用lambda表达式来创建匿名函数。
"""

#原始程序
MAXIMUM = lambda x,y: (x > y) * x + (x < y) * y
MINIMUM = lambda x,y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
	a = 10
	b = 20
	print('The larger one is %d' % MAXIMUM(a,b))
	print('The lower one is %d' % MINIMUM(a,b))

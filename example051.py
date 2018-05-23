#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example051.py
#Author: kernellmd 
#Created Time: 2018-05-23 07:45:05
############################  

"""
题目描述：练习按位与&的使用
"""

if __name__ == '__main__':
	a = 7  #0b111
	b = a & 3  #0b11
	print('a & 3 = %d' % b)
	b &= 5
	print('b & 5 = %d' % b)

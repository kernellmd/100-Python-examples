#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example079.py
#Author: kernellmd 
#Created Time: 2018-05-23 12:38:27
############################  

"""
题目描述:字符串排序
"""

if __name__ == '__main__':
	str1 = input('input string:')
	str2 = input('input string:')
	str3 = input('input string:')
	print(str1,str2,str3)

	if str1 > str2: str1,str2 = str2,str1
	if str1 > str3: str1,str3 = str3,str1
	if str2 > str3: str2,str3 = str3,str2

	print('after being sorted:')
	print(str1,str2,str3)

#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example062.py
#Author: kernellmd 
#Created Time: 2018-05-23 10:07:14
############################  

"""
题目描述：查找字符串。
程序分析：利用find函数
str.find(sub[, start[, end]])¶
Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

Note The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator:
>>>
>>> 'Py' in 'Python'
True
"""

#原始程序
sStr1 = 'abcdefg'
sStr2 = 'cde'
sStr3 = 'qq'

if sStr2 in sStr1:
    print(sStr1.find(sStr2))
else:
    print("%s is not in %s" %(sStr2, sStr1))

if sStr3 in sStr1:
    print(sStr1.find(sStr3))
else:
    print("%s is not in %s" %(sStr3, sStr1))

#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example054.py
#Author: kernellmd 
#Created Time: 2018-05-23 08:00:58
############################  

"""
题目描述：取一个整数a从右端开始的4-7位。
程序分析：可以这样考虑：
(1)先使a右移4位。
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
(3)将上面二者进行&运算。
"""

#原始程序
if __name__ == "__main__":
    a = 123  #0b1111011
    a >>= 4  #0b111
    print("result: %d" %(a & 15))
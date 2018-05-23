#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example055.py
#Author: kernellmd 
#Created Time: 2018-05-23 08:11:24
############################  

"""
题目描述：学习使用按位取反~。
程序分析：~0=1; ~1=0; ~a=-(a+1)
"""

if __name__ == '__main__':
    a = 234  #0b0000000000000000...11101010
    b = ~a  #0b11111111111111......00010101
    print('The a\'s 1 complement is %d' % b)  #对b按补码输出
    a = ~b
    print('The a\'s 2 complement is %d' % a)

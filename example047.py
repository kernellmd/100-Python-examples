#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example047.py
#Author: kernellmd 
#Created Time: 2018-05-22 19:05:50
############################  

"""
题目描述：两个变量值互换。
"""

#原始程序
if __name__ == "__main__":
    x = int(input("Please input x:"))
    y = int(input("Please input y:"))
    y, x = x, y
    print("x = %d y = %d" %(x, y))

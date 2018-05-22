#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example045.py
#Author: kernellmd 
#Created Time: 2018-05-22 18:51:37
############################  

"""
题目描述：统计 1 到 100 之和。
"""

#原始程序
if __name__ == "__main__":
    sum = 0
    for i in range(1, 101):
        sum += i
    print("The sum from 1 to 100 is %d" %(sum))

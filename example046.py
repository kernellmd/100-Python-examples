#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example046.py
#Author: kernellmd 
#Created Time: 2018-05-22 18:59:13
############################  

"""
题目描述：求输入数字的平方，如果平方运算后小于 50 则退出。
"""

#原始程序
if __name__ == "__main__":
    flag = True
    while flag:
        num =int(input("Please input a number:"))
        if num ** 2 < 50:
            flag = False

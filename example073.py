#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example073.py
#Author: kernellmd 
#Created Time: 2018-05-23 12:17:50
############################  

"""
题目描述：反向输出一个链表。
"""

#原始程序
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('input a number:'))
        ptr.append(num)

    print(ptr)
    ptr.reverse()
    print(ptr)

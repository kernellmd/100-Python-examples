#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example067.py
#Author: kernellmd 
#Created Time: 2018-05-23 10:44:30
############################  

"""
题目描述：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""

#原始程序
from random import seed
from random import randrange

def gener_random_seq(n):
    L = []
    for i in range(n):
        L.append(randrange(1, 10000))
    return L

if __name__ == "__main__":
    L = gener_random_seq(10)
    print(L)
    max = L[0]
    max_position = 0
    min = L[0]
    min_position = 0
    for i in range(10):
        if L[i] > max:
            max = L[i]
            max_position = i
        if L[i] < min:
            min = L[i]
            min_position = i
    L[0], L[max_position] = L[max_position], L[0]
    L[9], L[min_position] = L[min_position], L[9]
    print(L)

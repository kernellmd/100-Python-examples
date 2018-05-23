#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example068.py
#Author: kernellmd 
#Created Time: 2018-05-23 11:17:06
############################  

"""
题目描述：有n个整数，使其前面各数顺序向后移m个位置，
最后m个数变成最前面的m个数
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
    m = 3
    newL = L[10 - m:] + L[:10 - m]
    print(newL)

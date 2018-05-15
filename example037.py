#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
题目描述：对n个数进行排序。
程序分析：利用 Pyhton 内置函数sorted
"""

#原始程序
#生成随机数列
from random import seed
from random import randrange

def gener_randon_seq(n):
    L = []
    for i in range(n):
        L.append(randrange(1, 10000))
    return L

if __name__ == "__main__":
    L = gener_randon_seq(10)
    print("The sequence before sorting is:")
    print(L)
    print("The ordered sequence is:")
    print(sorted(L))

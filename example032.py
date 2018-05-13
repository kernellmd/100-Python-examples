#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：按相反的顺序输出列表的值。
程序分析：利用序列的操作
"""

#原始程序
#利用随机数生成序列
"""
从random模块中导入种子初始化函数seed
和随机数生成函数randrange
"""
from random import seed, randrange

def gener_rand_seq(n):
    L = []
    seed()
    #构造1~1000范围内的随机数序列
    for i in range(n):
        L.append(randrange(1, 1000))
    return L

def reverse_output(seq):
    for val in reversed(seq):
        print(val, end=" ")
    print()

if __name__ == "__main__":
    L = gener_rand_seq(5)
    print("Original sequence:")
    print(L)
    print("Reversed sequence:")
    reverse_output(L)

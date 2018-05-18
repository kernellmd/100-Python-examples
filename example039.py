#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
题目描述：有一个已经排好序的数组。现输入一个数，要求按原
        来的规律将它插入数组中。
程序分析：首先判断此数是否大于最后一个数，然后再考虑
        插入中间的数的情况，插入后此元素之后的数，依
        次后移一个位置。
"""

#这里利用了第三方numpy库
from numpy import arange

def insert(orig_list, num):
    position = 0
    for i in orig_list:
        if num < orig_list[i]:
            position = i
            break
    num = [num]
    insert_list = orig_list[: position] + num + orig_list[position :]
    return insert_list

if __name__ == "__main__":
    L = list(arange(0, 100, 5))
    num = int(input("Please input a number for inserting:"))
    print(insert(L, num))

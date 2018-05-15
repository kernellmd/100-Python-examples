#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
题目描述：求一个3*3矩阵对角线元素之和。
程序分析：利用for循环将arr[i][i]依次相加
"""

#利用列表实现
def arr_sum(arr, dimen):
    arr_sum = 0
    for i in range(dimen):
        arr_sum += arr[i][i]
    return arr_sum

if __name__ == "__main__":
    arr = [[1, 3, 5],
           [2, 5, 10],
           [3, 7, 18]]
    print("The original array is:")
    print(arr)
    print("The sum of this array is:")
    print(arr_sum(arr, 3))

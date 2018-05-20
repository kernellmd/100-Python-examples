#/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
题目描述：将一个数组逆序输出。
程序分析：直接利用内置的逆置函数即可
"""

#原始程序
if __name__ == "__main__":
    arr = [1, 4, 2, 19, 34, 7, 90, 35, 100]
    print("The original array is:")
    print(arr)
    print("The reversed array is:")
    print(list(reversed(arr))) #reversed返回一个迭代器
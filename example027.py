#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：利用递归函数调用方式，将所输入的5个字符，
        以相反顺序打印出来。
"""

def print_string(str, len):
    if len != 1:
        print(str[len - 1], end="-")
        print_string(str,len - 1)
    else:
        print(str[0])
    return

if __name__ == "__main__":
    str = input("Please input a string:")
    print_string(str, len(str))

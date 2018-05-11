#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：一个5位数，判断它是不是回文数。即12321是回文数，
        个位与万位相同，十位与千位相同。
程序分析：利用字符串工厂函数转换数字，然后用序列操作
"""

#原始程序
def is_palindrome_number(str_num):
    flag = True
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-1 - i]:
            flag = False
            break
    return flag

if __name__ == "__main__":
    num = input("Please input a number:")
    if is_palindrome_number(num):
        print("%s is a palindrome number!" %(num))
    else:
        print("%s is not a palindrome number!" %(num))

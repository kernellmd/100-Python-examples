#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：给一个不多于5位的正整数
        求：一、求它是几位数
            二、逆序打印出各位数字。
程序分析：利用求模和取余分解整数
"""
#原始程序
def digit_num(val):
    num = 0
    if val == 0:
        num = 1
    while val > 0:
        val //= 10
        num += 1
    return num

def reverse_print(val):
    if val == 0:
        print(val)
    while val > 0:
        tmp = val % 10
        val //= 10
        print(tmp, end="")
    else:
        print()

if __name__ == "__main__":
    val = int(input("Please input a number:"))
    print("The figure is %d digits." %(digit_num(val)))
    print("The reverse output of this number is:")
    reverse_print(val)

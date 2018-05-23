#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example076.py
#Author: kernellmd 
#Created Time: 2018-05-23 12:26:26
############################  

"""
题目描述：编写一个函数，输入n为偶数时，调用函数求
1/2+1/4+...+1/n,
当输入n为奇数时，调用函数1/1+1/3+...+1/n(利用指针函数)
"""

#原始程序
def sum_even(n):
    sum = 0
    for i in range(2, n + 1, 2):
        sum += 1 / i
    return sum

def sum_odd(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum += 1 / i
    return sum

if __name__ == "__main__":
    num = int(input("Please input a number:"))
    res = 0
    if num % 2 == 0:
        res = sum_even(num)
    else:
        res = sum_odd(num)
    print("The result is %f" %(res))

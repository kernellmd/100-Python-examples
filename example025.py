#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
"""
#原始程序
def factorial(n):
    factorial = 1; 
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += factorial(i)
    return sum

if __name__ == "__main__":
    print("the sum of factorial from 1 to 20 is %d" %(sum(20)))

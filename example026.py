#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：利用递归方法求5!。
程序分析：递归公式：f(n)!=n*f(n-1)!
"""
def factorial_recursion(n):
    if n > 1:
        return n * factorial_recursion(n - 1)
    else:
        return 1

if __name__ == "__main__":
    print("the value of the factorial obtained through recursion is %d."
          %(factorial_recursion(5)))

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
题目描述：求1~n之内的素数。
程序分析：判断素数的方法，原始的是用除了1和自身外的
        其他数去除那个数，如果都不能除尽，就是，否则
        就不是。
        一个简化的方法就是没必要用2~n-1去除，只需要
        用2~sqrt(n)去除就可以。
        一个更加简化的方法是用2~sqrt(n)范围内的素数
        去除
        一个更加更加简化的方法是用
        “埃拉托色尼(Eratosthenes)筛法”，他是古希腊的著
        名数学家。他采取的方法是，在一张纸上写上1到n的
        全部整数，然后逐个判断它们是否是素数，找出一个
        非素数，就把它挖掉，最后剩下的就是素数。
"""

import sys

def prime(n):
    flag = [1]*(n+2)
    p=2
    while(p<=n):
        print(p, end=" ")
        for i in range(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break

if __name__ == "__main__":
    n = int(input("Please input a number:"))
    print("The following are the prime numbers from 1 to %d:" %(n))
    prime(n)
    print()

#!/usr/bin/env python3.6
# -*  coding: utf-8 -*-
"""
题目描述：一个数如果它所有的真因子（即除了自身以外的约数）的和，恰好等于它本身，则
          称该数为完数。例如6=1＋2＋3。编程找出1000以内的所有完数。
程序分析：利用for循环求出所有约数，利用sum计算所有约数之和是否为原整数
"""
#原始程序
#求约数，并将所有的约数装到列表中返回
def divisor(n):
    L = [1]
    for i in range(2, n):  #还有优化空间，循环到 ceil(n / 2) + 1 就可以
        if n % i == 0:
            L.append(i)
        else:
            continue
    return L

#判断一个数是否为完全数
def is_perfect_number(var):
    tmp = divisor(var)
    if var == sum(tmp):
        return True
    else:
        return False

if __name__ == "__main__":
    for i in range(2, 1000):
        if is_perfect_number(i):
            print(i)
        else:
            continue

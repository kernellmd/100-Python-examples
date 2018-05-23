#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example069.py
#Author: kernellmd 
#Created Time: 2018-05-23 11:40:57
############################  

"""
题目描述：有n个人围成一圈，顺序排号。从第一个人开始报数
（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来
第几号的那位。
"""

#原始程序
def last(n):
    L = [True] * n
    count = 0
    while True:
        for i, flag in enumerate(L):
            if flag == True:
                count += 1
                if count == 3:
                    count = 0
                    L[i] = False
                    n -= 1
                    if n == 0:
                        return i

if __name__ == "__main__":
    n = int(input("Please input a number:"))
    position = last(n)
    #注意数组的序号和实际序号的差别
    print("The last position is %d" %(position))

#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example066.py
#Author: kernellmd 
#Created Time: 2018-05-23 10:18:49
############################  

"""
题目描述：输入3个数a,b,c，按大小顺序输出。　　
程序分析：利用if语句简洁比较
"""

if __name__ == '__main__':
    n1 = int(input('n1 =:'))
    n2 = int(input('n2 =:'))
    n3 = int(input('n3 =:'))

    if n1 > n2:
            n1, n2 = n2, n1
    if n1 > n3:
            n1, n3 = n3, n1
    if n2 > n3:
            n2,n3 = n3, n2

    print(n1,n2,n3)

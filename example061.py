#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example061.py
#Author: kernellmd 
#Created Time: 2018-05-23 09:28:22
############################  

"""
题目描述：打印出杨辉三角形（要求打印出rows行如下图）。　　
程序分析：构造一个二位数组，利用杨辉三角的特性填充二位数组
"""

def create_PascalTriangle(rows):
    a = []
    for i in range(rows):
            a.append([])
            for j in range(rows):
                    a[i].append(0)
    for i in range(rows):
            a[i][0] = 1
            a[i][i] = 1
    for i in range(2,rows):
            for j in range(1,i):
                    a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(rows):
            for j in range(i+1):
                    print(str(a[i][j]), end=" ")
            print()

if __name__ == "__main__":
    create_PascalTriangle(10)

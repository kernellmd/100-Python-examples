#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
题目描述：求sum=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
        例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加
        由键盘控制。
程序分析：利用循环或lambda表达式
"""
#改进
#lambda表达式使程序可读性降低，
#改用for in if结构替换lambda表达式
def sum(n, digit):
    sum = 0
    tmp = digit
    for i in range(n):  #进行n次循环相加
        for j in range(i):  #产生下一个加数
            tmp *= 10
            tmp += digit
        sum += tmp  #相加，并将tmp置为digit
        tmp = digit
    return sum

if __name__ == '__main__':
    n = int(input('input number:') )
    digit = int(input('input digit:'))
    sum = sum(n, digit)
    print('the value of expression is: %d' %(sum))

#原始程序
#利用列表和lambda表达式
#import functools

#def sum(n, digit):
#    tmp = digit
#    L = []
#    for i in range(n):
#        L.append(tmp)
#        tmp *= 10
#        tmp += digit

#    return functools.reduce(lambda x, y: x + y, L)

#if __name__ == '__main__':
#    n = int(input('input number:') )
#    digit = int(input('input digit:'))
#    sum = sum(n, digit)
#    print('the value of expression is: %d' %(sum))

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
题目描述：猴子吃桃问题：猴子第一天摘下若干个桃子，
          当即吃了一半，还不瘾，又多吃了一个第二天早上又
          将剩下的桃子吃掉一半，又多吃了一个。以后每天早上
          都吃了前一天剩下的一半零一个。到第10天早上想再吃时，
          见只剩下一个桃子了。求第一天共摘了多少。
程序分析：采取逆向思维的方法，从后往前推断
"""

#原始程序
def sum_peach(rest, day):
    day -= 1
    while day:
        rest += 1
        rest *= 2
        day -= 1
    return rest

if __name__ == '__main__':
    rest = sum_peach(1, 10)
    print(rest)

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
题目描述：一球从100米高度自由落下，每次落地后反跳回原高度
          的一半；再落下，求它在第10次落地时，共经过多少米？第10
          次反弹多高？
程序分析：利用for循环进行迭代
"""
#原始程序
#根据下落高度和落地次数求总距离和最后一个落地弹跳的高度
def get_distance(height, time):
    if time == 1:
        return height, height / 2
    else:
        #第一次落地
        distance = height
        #第二次到第time次
        for i in range(1, time):
            distance += height
            height /= 2
        return distance, height / 2
        
if __name__ == '__main__':
    print(get_distance(100, 10))

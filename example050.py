#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: example050.py
#Author: kernellmd 
#Created Time: 2018-05-22 19:26:15
############################  

"""
题目描述：输出一个随机数。
程序分析：使用 random 模块。
"""

#原始程序
import random

#生成10到20之间的随机数
#uniform() 方法将随机生成下一个实数，它在[x,y]范围内。
print(random.uniform(10,20))

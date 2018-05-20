#/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
题目描述：python动态语言特性
"""

#原始程序
class test(object):
    pass

t = test()
print(t.count) # 会出错，因为count不存在
t.count = 1
print(t.count) # 不会出错，因为新创建了一个count
#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：按逗号分隔列表。
1、join()函数：
语法：  'sep'.join(seq)
参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一
个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串
2、os.path.join()函数
语法：  os.path.join(path1[,path2[,......]])
返回值：将多个路径组合后返回
"""

def style(L):
    #join（）必须传入一个可迭代对象
    #详见官方文档str.join函数
	sl = ' '.join(str(n) for n in L)
	print(sl)

if __name__ == '__main__':
    L = [1,2,3,4,5]
    print("Original sequence:")
    print(L)
    print("Formatted sequence:")
    style(L)

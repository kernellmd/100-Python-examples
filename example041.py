#/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
题目描述：学习static定义静态变量的用法
"""

#python没有static关键字，可以用函数本地变量做某种程度的实现
def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()

##python动态语言特性
#class test(object):
#    pass

#t = test()
#print(t.count) # 会出错，因为count不存在
#t.count = 1
#print(t.count) # 不会出错，因为新创建了一个count
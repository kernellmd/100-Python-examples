#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：有5个人坐在一起，问第五个人多少岁？他说比
        第4个人大两岁。问第4个人岁数，他说比第3个人大两岁。
        问第3个人，又说比第2人大两岁。问第2个人，说比
        第一个人大两岁。最后问第1个人，他说是10岁。请
        问第五个人多大？
程序分析：利用递归的方法，递归分为递推与回归两个阶
        段。要想知道第五个人岁数，需知道第四人的岁数，
        依次类推，推到第一人（10岁），再往回推。
"""
#改进1
#将递归函数的返回改变为单一出口
def age_one_exit(n):
    if n == 1:
        age = 10
    else:
        age = age_one_exit(n -1) + 2
    
    return age

if __name__ == "__main__":        
    print("the age of %d# person is %d" %(5, age_one_exit(5)))

#原始程序
def age(n):
    if n == 1:
        return 10
    else:
        return age(n -1) + 2

#if __name__ == "__main__":        
#    print("the age of %d# person is %d" %(5, age(5)))

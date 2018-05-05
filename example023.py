#!usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
题目描述：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
程序分析：先把图形分成两部分来看待，前四行
          一个规律，后三行一个规律，利用双重for循环，
          第一层控制行，第二层控制列
          每一部分分为两个工作，打印空格和打印*号
"""
#使用常数变易法对程序进行改进
def draw():
    for i in range(1, 5):
        #每行需要打印空格数的一半
        tmp = int((7 - (2 * i - 1)) / 2)
        for j in range(tmp):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        for m in range(tmp):
            print(" ", end="")
        print()    

    for i in range(3, 0, -1):
        #每行需要打印空格数的一半
        tmp = (7 - (2 * i - 1)) // 2
        for j in range(tmp):
            print(" ", end="")
        for x in range(2 * i - 1):
            print("*", end="")
        for j in range(tmp):
            print(" ", end="")
        print()

if __name__ == "__main__":
    draw()

#原始程序
def draw():
    print("   *   ")
    print("  ***  ")
    print(" ***** ")
    print("*******")
    print(" ***** ")
    print("  ***  ")
    print("   *   ")

#if __name__ == "__main__":
#    draw()

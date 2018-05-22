#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
题目描述：利用类变量代替静态变量
'''
class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()

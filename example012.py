"""
题目描述：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt
(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""
from math import *

def is_prime(x):
    #注意range的第二个参数不能是ceil(sqrt(x))
    #因为sqrt返回的是浮点数，不精确
    #也可以用int代替ceil
    for var in range(2, ceil(sqrt(x)) + 1):
        if x % var == 0:
            return False
    return True
  
def count():
    num = 0
    for i in range(101, 201):
        if is_prime(i):
            #assert(i != 121)
            #print(i)
            num += 1
    return num

if __name__ == '__main__':
    print(count())

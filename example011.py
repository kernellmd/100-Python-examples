"""
题目描述：古典问题：有一对兔子，从出生后第3个月起每个月都
生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子对数的规律为数列1,1,2,3,5,8,13,21....
实际上还是斐波那契数列问题。
"""

def fib(n):
    l = [1, 1]
    count = 2
    if n == 1:
        return l[0]
    elif n == 2:
        return l[1]
    else:
        while count < n:
            l.append(l[-2] + l[-1])
            count += 1
        return l[-1]

def count_rabb():
    n = int(input('求第n个月兔子总数，n='))
    print(fib(n))

if __name__ == '__main__':
    count_rabb()

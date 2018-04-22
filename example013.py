"""
题目描述：打印出所有的"水仙花数"，所谓"水仙花数"是指一个
三位数，其各位数字立方和等于该数本身。例如：153是一
个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，
十位，百位。
三次方：**3
"""

#n = int(input('打印小于n的所有的水仙花数（三位数），n='))

def narc_num(L):
    for x in range(100, 1000):
        ones = x % 10
        tens = (x // 10) % 10
        hundreds = x // 100
        if x == ones ** 3 + tens ** 3 + hundreds ** 3:
            L.append(x)

if __name__ == '__main__':
    L = []
    narc_num(L)
    print(L)
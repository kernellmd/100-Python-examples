"""
题目描述：有一分数序列：2/1，3/2，5/3，8/5，
        13/8，21/13...求出这个数列的前20项之和。
程序分析：注意分子与分母的变化规律。把分数分为
        两部分看，分子和分母分成两个单独的数来对待
"""

#原始程序
#生成数列
def create_series(n):
    numerator = [2]
    denominator = [1]
    for i in range(n - 1):
        numerator.append(numerator[i] + denominator[i])
        denominator.append(numerator[i])
    series = []
    for i in range(n):
        series.append(numerator[i] / denominator[i])
    return series

if __name__ == "__main__":
    sum = sum(create_series(20))
    #注意不是%d
    print("the sum of first twenty items of the series is %f." %(sum))

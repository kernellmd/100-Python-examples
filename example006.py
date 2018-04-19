"""
题目描述：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""

n = int(input('输出斐波那契数列前n项，n ='))

#迭代方式
def fib_iter(n):
    l = [0, 1]
    count = 2
    while count < n:
        #此处用切片方式也可以
        #x, y = l[-2:]
        #l.append(x + y)
        l.append(l[-2] + l[-1])
        count += 1
    print(l)

#递归方式
def fib_recur(n):
    l = [0, 1]
    def fib():
        #此处不可用切片方式
        #切片（slice）操作不改变原序列，而是生成一个新序列
        #要注意区分切片和索引操作，即使只切一个值
        l.append(l[-1] + l[-2])
        if len(l) < n:
            fib()
    fib()
    print(l)

def main():
    #fib_iter(n)
    fib_recur(n)

if __name__ == '__main__':
    main()

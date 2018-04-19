"""
题目描述：输出9*9乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""
#改进
#range(1,10)可读性更好，程序更加清爽
def main():
    for i in range(1, 10):
        for j in range(1, 10):
            if j <= i:
                print('%d * %d = %d' \
                       %(j, i, i * j), end = '   ')
        print()
        
if __name__ == '__main__':
    main()


#原始程序
#def main():
#    for i in range(9):
#        for j in range(9):
#            if j <= i:
#                print('%d * %d = %d' \
#                       %(j + 1, i + 1, (i + 1) * (j + 1)), end = '   ')
#        print()
        
#if __name__ == '__main__':
#    main()

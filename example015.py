"""
题目描述：利用条件运算符的嵌套来完成此题：学习成绩>=90分
的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""

def rate(score):
    if score >= 90:
        return 'A'
    elif score >= 60:
        return 'B'
    else:
        return 'C'

if __name__ == '__main__':
    score = int(input('input score:'))
    rat = rate(score)
    print('rate:', rat)

"""
题目描述：暂停一秒输出。
程序分析：需要time模块。
"""

#原始程序
from time import sleep

def main():
    print('start!')
    sleep(1)
    print('Pause for 1 second...')

if __name__ == '__main__':
    main()
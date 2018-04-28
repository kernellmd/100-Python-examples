"""
题目描述：输入一行字符，分别统计出其中英文字母、空格、
        数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#原始程序
def is_chinese(uchar):
    if uchar >= u'\u4E00' and uchar <= u'\u9FA5':
        return True
    else:
        return False

def is_english(uchar):
    if ( uchar >= u'\u0041' and uchar <= u'\u005A' ) or ( uchar >= u'\u0061' and uchar <= u'\u007A'):
        return True
    else:
        return False

def statistics(s):
    letter_cn = 0
    letter_en = 0
    space = 0
    numeric = 0
    others = 0
    for c in s:
        if is_english(c):
            letter_en += 1
        elif is_chinese(c):
            letter_cn += 1
        elif c.isdigit():
            numeric += 1
        elif c == u'\u0020':
            space += 1
        else:
            others += 1
    return letter_cn, letter_en, space, numeric, others

if __name__ == '__main__':
    s = input('input a string:')
    letter_cn, letter_en, space, numeric, others = statistics(s)
    print('the number of en is %d' %(letter_en))
    print('the number of cn is %d' %(letter_cn))
    print('the number of space is %d' %(space))
    print('the number of numeric is %d' %(numeric))
    print('the number of other chars is %d' %(others))    

'''
#test
#判断是否是汉字
def is_chinese(uchar):
    if uchar >= u'\u4E00' and uchar <= u'\u9FA5':
        return True
    else:
        return False

#判断是否是英文字母
def is_english(uchar):
    if ( uchar >= u'\u0041' and uchar <= u'\u005A' ) or ( uchar >= u'\u0061' and uchar <= u'\u007A'):
        return True
    else:
        return False

if __name__ == '__main__':
    c = input('input a char:')
    if is_chinese(c):
        print('%s is a chinese char!' %(c))
    elif c.isdigit():
        print('%s is a number!' %(c))
    elif is_english(c):
        print('%s is a english char!' %(c))
'''
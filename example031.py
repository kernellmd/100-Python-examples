#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

"""
题目描述：请输入星期几的第一个字母来判断一下是星期几，
		如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，
		则判断用情况语句或if语句判断第二个字母。。
		要求复杂了可以加入大小写字母转换
"""

#原始程序
def week_judge():
    dict_first_letter = {
                         'm': 'Monday',
                         'M': 'Monday',
                         'f': 'Friday',
                         'F': 'Friday',
                         'w': 'Wednesday',
                         'W': 'Wednesday'
                         }
    dict_first_two_letters = {
                              'su': 'Sunday',
                              'Su': 'Sunday',
                              'sa': 'Saturday',
                              'Sa': 'Saturday',
                              'tu': 'Tuesday',
                              'Tu': 'Tuesday',
                              'Th': 'Thursday',
                              'th': 'Thursday'
                             }
    try:
        letter1 = input("Please input the first letter of the week:")
        if letter1 in dict_first_letter:
            print("Oh!It's %s." %(dict_first_letter[letter1]))
        else:
            print("The first letter is not enough to judge!")
            letter2 = input("Please input the second letter of the week:")
            letters = letter1 + letter2
            print("God!It's %s!!!" %(dict_first_two_letters[letters]))
    except Exception as e:
        print("Incorrect input, please read the tips carefully!")
        print(e)

if __name__ == "__main__":
    week_judge()

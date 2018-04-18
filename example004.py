'''
题目描述：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然
        后再加上5天即本年的第几天，特殊情况，闰年且
        输入月份大于3时需考虑多加一天。
'''
#改进
year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))

#使用元组记录一组常数
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)


#原始程序
'''
January = 31
February = 29
February_leap = 30
March = 31
April = 30
May = 31
June = 30
July = 31
August = 31
september = 30
October = 31
November = 30
December = 31

def IsLeap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def main():
    year = int(input('year:'))
    month = int(input('month:'))
    day = int(input('day:'))

if __name__ == '__main__':
    main()
'''
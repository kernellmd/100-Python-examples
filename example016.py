"""
题目描述：输出指定格式的日期。
程序分析：调用time模块或datetime模块进行格式化输出
"""

#改进
'''
datetime模块以面向对象的形式对很多使用功能进行了封装，
比起time模块更加好用，time模块具有的功能在datetime
模块下都有实现，只是直接使用繁琐一点
'''

from datetime import *
d = date.today()
print(d.strftime('%Y %m %d'))

dt = datetime.now()
print(dt.date())
print(dt.time())
print(dt.strftime('%Y %m %d %H:%M:%S'))

#完全可以使用datetime模块来获取时间按戳
print(datetime.now().timestamp())

'''
使用 time 模块下的strftime函数，可以方便的输出格式化的时间字符串，
time 模块更接近操作系统底层，围绕 Unix Timestamp 进行。该模块中的，
很多函数调用了C Library，具有很强的平台相关性
from time import *
print(time())  #返回Unix Timestamp
print(localtime()) # 返回UTC时间
print(gmtime())    # 返回本地时间，在中国就是UTC+8

#时间格式化输出
print(strftime('%c'))
print(strftime('%A %B %d %U %H:%M:%S %Y'))
#s = '与UTC时间的差值：'
#print(s.encode('utf-8'))
print(strftime('the gap with UTC: %z'))
print(strptime("30 Nov 00", "%d %b %y"))
'''
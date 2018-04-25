#使用time模块下的process_time()
#函数计算程序运行时间，不包括sleep时间
import time

print(time.process_time())

#time.sleep(2)
sum = 0
for i in range(1000000):
    sum += i

print(time.process_time())

'''
#isinstance 和 type的区别
class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))  # returns True
print(type(A()) == A)    # returns True
print(isinstance(B(), A))    # returns True
print(type(B()) == A)    # returns False
'''
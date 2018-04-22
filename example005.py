"""
题目描述：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，
        如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
        如果x>z则将x与z的值进行交换，这样能使x最小。
"""
#改进
l = []
for i in range(3):
	x = int(input('第%d个整数：' % (i+1)))
	l.append(x)
print(l)

'''
sort和sorted区别：
sorted和sort 的区别主要在于sorted是将排序完的数据赋予
给一个新变量，而sort则是在原变量的基础上直接进行排序，不
产生新变量,无返回值
'''
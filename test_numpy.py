#import numpy as np
from numpy import array
from numpy import zeros
from numpy import ones
from numpy import int
from numpy import arange
from numpy import linspace

arr = array([[1, 3, 5, 9],
             [2, 4, 8, 18],
             [3, 5, 10, 37]])

print(arr)
#获取数组的维数，当前是二维数组
print("number of dim:", arr.ndim)
print("shape", arr.shape)
print("size:", arr.size)
#获取矩阵中数据的类型
print(arr.dtype)

#定义3行4列全部为0的矩阵
arr_zero = zeros((3, 4))
print(arr_zero)

#定义3行4列全部为1的矩阵，并且数据类型为整型
#也可以定义为int16或int32或int64
arr_one = ones((3, 4), dtype=int)
print(arr_one)

#定义一维数列矩阵
arr_one_dimen = arange(1, 10, 2) #步长值为2
print(arr_one_dimen)

#重新定义数列的行列
arr_reshape = arange(12).reshape(3, 4)
print(arr_reshape)

#某一个范围内固定数目的值组成数列
arr_linspace = linspace(1, 10, 12).reshape((3, 4))
print(arr_linspace)

#数组减法
arr1 = array([1, 4, 8, 10])
arr2 = arange(4)
print(arr1, arr2) #输出原数组
diff = arr1 - arr2
print("the diff is", diff) #输出两个数组作差后的数组
sum_plus = arr1 + arr2
print("the sum is ", sum_plus) #输出两个数组的和

#对矩阵中每个数字平方
arr_cube = array([[1, 5, 11],
                 [2, 8, 20]])
arr_cube_res = arr_cube ** 2
print(arr_cube_res)

#求sin值(tan，cos类似)
from numpy import sin
arr_sin = array([4, 10, 38])
arr_sin_res = sin(arr_sin)
print(arr_sin_res)

#判断矩阵中的值
arr_comp = arange(6).reshape((3, 2))
print(arr_comp)
print(arr_comp < 3)

#对应数字相乘
arr_cheng1 = arange(4).reshape((2, 2))
print("arr_cheng1:", arr_cheng1)
arr_cheng2 = arange(5, 9).reshape((2, 2))
print("arr_cheng2:", arr_cheng2)
print("ji:", arr_cheng1 * arr_cheng2)

#矩阵乘法
from numpy import dot
arr_multi_1 = arange(4).reshape((2, 2))
print("multiplier1:", arr_multi_1)
arr_multi_2 = arange(5, 9).reshape((2, 2))
print("multiplier2:", arr_multi_2)
print("product:", dot(arr_multi_1, arr_multi_2))
#第二种矩阵乘法的形式
print("product2:", arr_multi_1.dot(arr_multi_2))

#随机生成矩阵
from numpy import random
arr_random = random.random((3, 4))
print(arr_random)

#求矩阵的和、最小值和最大值
#还控制在一列(aixs=0)或一行(aixs=1)中寻找
from numpy import sum, min, max
print("The min value of the arr is:", min(arr_random))
print("The max value of the arr is:", max(arr_random))
print("The sum of the arr is:", sum(arr_random))

#获取最小值和最大值的索引
from numpy import argmin, argmax
arr_arg = random.random((3, 4))
print(arr_arg)
print("The position of the min is:", argmin(arr_arg))
print("The position of the max is:", argmax(arr_arg))
#获取平均值mean
from numpy import mean
print("The mean of the array is:", mean(arr_arg))
print("The mean of the array is:", arr_arg.mean())
#获取平均值average
from numpy import average
print("The mean of the array is:", average(arr_arg))
#获取中位数
from numpy import median
print("The mean of the array is:", median(arr_arg))
#依次累加和，类似斐波那契数列
from numpy import cumsum
arr_cumsum = arange(1, 13).reshape((3, 4))
print(arr_cumsum)
print("The result of 'cumsum' is:", cumsum(arr_cumsum))
#依次累差，最后会少一列，因为每个结果都是前一列对应数
#字与后一列对应数字之差
from numpy import diff
print("The result of 'diff' is:", diff(arr_cumsum))

#输出非零值对应的行数和列数
from numpy import nonzero
print("The positon of the nonzero is:",
      nonzero(arr_cumsum))

#逐行排序
from numpy import sort
arr_sort = arange(14, 2, -1).reshape((3, 4))
print("The array before sorting:\n", arr_sort)
print("The ordering array:\n", sort(arr_sort))

#矩阵转置，可以用transpose函数或者T属性
from numpy import transpose
print("The transpose:\n", transpose(arr_sort))
print("The T:\n", arr_sort.T)

#削波函数，将所有大于max的值改为max，小于min的值改为min
#范围内的数值不变
from numpy import clip
print("The result of the clip function:\n",
        clip(arr_sort, 5, 9))

#索引
arr_idx = arange(3, 15)
print("The original array is:\n", arr_idx)
print("The third value of the array is:\n",
        arr_idx[3]) #一维索引
arr_idx_two_dimen = arange(12).reshape((3, 4))
print("The original array is:\n", arr_idx_two_dimen)
print("The second row of the array is:\n",
        arr_idx_two_dimen[2]) #对行数的索引
print("The vale of [1][1] is:\n",
        arr_idx_two_dimen[1][1]) #对矩阵中特定位置的值索引
print("The vale of [1][1] is:\n",
        arr_idx_two_dimen[1, 1])#另一种形式
print("The second row of the array is:\n",
        arr_idx_two_dimen[1, :]) #类似与列表中的冒号，打印出第二行的所有数
print("The second column of the array is:\n",
        arr_idx_two_dimen[:, 1]) #打印出第一列的所有数
print("The value of [1, 1:3]:\n",
        arr_idx_two_dimen[1, 1:3]) #打印出第一行第一和第二个数

#for循环迭代
#对每一行迭代
print("Iterate on rows of the matrix:")
for row in arr_idx_two_dimen:
    print(row)
#对每一列迭代
print("Iterate on columns of the matrix:")
for column in arr_idx_two_dimen.T: #这里利用了转置
    print(column)

#flatten可将矩阵变为一维数组，flat则返回对应的迭代器
print("The 1-dimen array:\n", arr_idx_two_dimen.flatten())
print("The items in matrix:")
for item in arr_idx_two_dimen.flat:
    print(item)

#矩阵合并
from numpy import hstack
from numpy import vstack
arr_merge1 = array([1, 1, 1])
arr_merge2 = array([2, 2, 2])

arr_merge_v = vstack((arr_merge1, arr_merge2)) #垂直合并
print("The shape before merging vertically:", arr_merge1.shape)
print("The shape after merging:", arr_merge_v.shape)
arr_merge_h = hstack((arr_merge1, arr_merge2)) #水平合并
print("The shape after merging horizontally:", arr_merge_h.shape)

#一维数列的转置，transpose和T无法实现
#使用reshap(arr.size, 1)
arr_transpose_1 = arr_merge1.reshape(arr_merge1.size, 1)
print("Transpose from 1-dimen array:\n", arr_transpose_1)
#还可以通过加维度的方法转置一维数组
from numpy import newaxis
print(arr_merge1[:, newaxis])

#利用concatnate合并
from numpy import concatenate
print("Merge multiple arrays:\n", concatenate((arr_merge1, arr_merge2,
    arr_merge1), axis=0))

#分割矩阵
from numpy import split
arr_partiton = arange(12).reshape((3, 4))
print("The original array:\n", arr_partiton)
print(split(arr_partiton, 2, axis=1)) #横向分成对等的两列
print(split(arr_partiton, 3, axis=0)) #纵向分割成3行
#不等分割
from numpy import array_split
print(array_split(arr_partiton, 3, axis=1)) #横向分成不对等的三列

#简化的分割函数
from numpy import vsplit
from numpy import hsplit
print("simply split:")
print(vsplit(arr_partiton, 3))
print(hsplit(arr_partiton, 2))
#使用copy函数可以直接进行深拷贝

#import numpy as np
from numpy import dot
from numpy import sin
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
sum = arr1 + arr2
print("the sum is ", sum) #输出两个数组的和

#对矩阵中每个数字平方
arr_cube = array([[1, 5, 11],
                 [2, 8, 20]])
arr_cube_res = arr_cube ** 2
print(arr_cube_res)

#求sin值(tan，cos类似)
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
arr_multi_1 = arange(4).reshape((2, 2))
print("multiplier1:", arr_multi_1)
arr_multi_2 = arange(5, 9).reshape((2, 2))
print("multiplier2:", arr_multi_2)
print("product:", dot(arr_multi_1, arr_multi_2))

"""
题目描述：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]
"""

#原始列表
l = [x for x in range(10)]
#print('初始列表为：', end = '')
print('初始列表为：', l)
#并没有真正复制，知识增加了一个指向列表的标识符
#l_copy1 = l
#l[0] = 3,会同时改变l[0]和l_copy1[0]
#print(l)

l_copy2 = l[:]
#l_copy2[1] = 100
print('第一种方式复制后的列表为：', l_copy2)
l_copy3 = list(l)
#l_copy3[2] = 200 
print('第三种方式复制后的列表为：', l_copy3)
#Python三元表达式有以下几种书写方法
if __name__ == '__main__':
    a = ''
    b = 'True'
    c = 'False'

    #方法一：为真时的结果 if 判定条件 else 为假时的结果  
    d = b if a else c
    print('方法一输出结果：' + d)

    #方法二：判定条件 and 为真时的结果 or 为假时的结果  
    d = a and b or c
    print('方法二输出结果：' + d)

    #以上两种方法方法等同于if ... else ...  
    if a:
        d = b
    else:
        d = c
    print('if语句的输出结果：' + d)
"""
说明：

判断条件：a为空串，所以判断条件为假

当判断条件为真时的结果：d = b

当判断条件为假时的结果：d = c
"""

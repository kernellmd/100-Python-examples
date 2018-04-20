'''
题目描述：要求输出国际象棋棋盘。
程序分析：用i控制行，j来控制列，根据i+j的和的变化来控制输出黑方格，还是白方格。
'''

#改进2
#通过代码重用优化程序
#定义一个绘制正方形的函数
import turtle
def drawSquare():
    turtle.pendown()  
    turtle.forward(10)  
    turtle.left(90)  
    turtle.forward(10)  
    turtle.left(90)  
    turtle.forward(10)  
    turtle.left(90)  
    turtle.forward(10)  
    turtle.left(90)  
    turtle.penup()

#在主函数中调用drawSquare()函数
def main():
    turtle.speed(30)  
    turtle.penup()  
    off = True  
    for y in range(-40, 30 + 1, 10):  
        for x in range(-40, 30 + 1, 10):  
            if off:  
                turtle.goto(x, y)  
                turtle.begin_fill()  
                turtle.color("black")  
                drawSquare()  
                turtle.end_fill()  
                turtle.penup()  
            else:  
                turtle.goto(x, y)  
                drawSquare()  
            off = bool(int(off) - 1)  
        off = bool(int(off) - 1)  
    turtle.hideturtle()  
    turtle.done()

if __name__ == '__main__': 
    main()

#改进1
#调用Python图形工具turtle绘制国际象棋棋盘
#import turtle  
#turtle.speed(30)  
#turtle.penup()  #提起笔移动，不绘制图形，用于另起一个地方绘制
#off = True  
#for y in range(-40, 30 + 1, 10):  #正数步长值，最后一个值小于stop
#    for x in range(-40, 30 + 1, 10):  
#        if off:  
#            turtle.goto(x, y) #将画笔移动到坐标为x,y的位置  
#            turtle.pendown()  
#            turtle.begin_fill()  
#            turtle.color("black")  
#            turtle.forward(10)  #向当前画笔方向移动10像素长
#            turtle.left(90)  #逆时针移动90°
#            turtle.forward(10)  
#            turtle.left(90)  
#            turtle.forward(10)  
#            turtle.left(90)  
#            turtle.forward(10)  
#            turtle.left(90)  
#            turtle.end_fill()  
#            turtle.penup()  
#        else:  
#            turtle.goto(x, y)  
#            turtle.pendown()  
#            turtle.forward(10)  
#            turtle.left(90)  
#            turtle.forward(10)  
#            turtle.left(90)  
#            turtle.forward(10)  
#            turtle.left(90)  
#            turtle.forward(10)  
#            turtle.left(90)  
#            turtle.penup()  
#        off = bool(int(off) - 1)  
#    off = bool(int(off) - 1)  
#turtle.hideturtle() #隐藏画笔的turtle形状 
#turtle.done()

#原始程序
#import sys
#for i in range(8):
#    for j in range(8):
#        if(i + j) % 2 == 0:
#            sys.stdout.write(chr(219))
#            sys.stdout.write(chr(219))
#        else:
#            sys.stdout.write(' ')
#    print('\n')
"""
    作者：瓜瓜
    功能：五角星绘制
    版本号：1.0
    日期：19.1.7
    增加功能: 绘制5个五角星
"""
import turtle

def main():
    """
    主函数
    :return:
    """
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.speed(10)
    turtle.pencolor('green')


    length =200
    pentagram(length)
    turtle.exitonclick()
def pentagram(length):
    count = 1
    while count <= 5:
        turtle.forward(length)
        turtle.right(144)
        count = count + 1
    length += 20
    if length < 300:
        pentagram(length)
    return



if __name__ == '__main__':
    main()
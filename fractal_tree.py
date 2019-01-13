"""
    作者：瓜瓜
    功能：分形树绘制
    版本号：1.0
    日期：19.1.10
    功能:利用递归函数绘制分形树
"""
import turtle


def draw_branch(length):
    """
    绘制分形树枝

    """
    # 绘制右侧树枝
    if length > 5:
        turtle.forward(length)
        print('向前',length)
        turtle.right(20)
        print('右转20')
        draw_branch(length-20)
        #绘制左侧树枝
        turtle.left(40)
        print("左转40")
        draw_branch(length-20)
        #返回之前的树枝
        turtle.right(20)
        print('右转20')
        turtle.backward(length)
        print('后退',length)



def main():
    """
    主函数
    :return:
    """
    turtle.penup()
    turtle.right(90)
    turtle.forward(200)
    turtle.right(180)
    turtle.pendown()
    turtle.speed(1)
    turtle.pencolor('green')
    draw_branch(45)
    turtle.exitonclick()




if __name__ == '__main__':
    main()
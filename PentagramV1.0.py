"""
    作者：瓜瓜
    功能：五角星绘制
    版本号：1.0
    日期：19.1.7
"""
import turtle

def main():
    """
    主函数
    :return:
    """
    length =200
    while  length< 300:
        pentagram(length,144)
        length = length + 20
    turtle.exitonclick()
def pentagram(length, degree):
    count = 1
    while count <= 5:
        turtle.forward(length)
        turtle.right(144)
        count = count + 1
    return



if __name__ == '__main__':
    main()
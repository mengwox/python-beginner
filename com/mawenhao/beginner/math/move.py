import math


def move(x, y, step, angle=0):
    """
    二维空间计算终点的坐标
    :param x: 起点x坐标
    :param y: 起点y坐标
    :param step: 起点与终点的距离
    :param angle: 两点的角度
    :return: 终点的(x,y)坐标
    """
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# 测试计算函数
x = 0
y = 0
step = 1
angle = 1
print(move(x, y, step, angle))

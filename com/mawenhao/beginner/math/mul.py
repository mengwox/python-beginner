# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def mul(x, *args):
    """
    计算一个或多个数的乘积
    :param x: 基数x
    :param args: 可变参数,用于接受多个数
    :return: 乘积
    """
    res = x
    for y in list(args):
        res *= y
    return res


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

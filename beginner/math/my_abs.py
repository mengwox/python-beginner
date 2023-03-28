def mwh_abs(x):
    """
    校验入参x是否是整数或浮点数?

    如果不是,则报错提示返回; 否则,则返回值的绝对值
    :param x: 入参
    :return: 绝对值
    :except TypeError 入参不符合类型
    """
    if not isinstance(x, (int, float)):
        raise TypeError('您输入的无法转为数字')
    else:
        if x > 0:
            return x
        else:
            return -x


# 测试绝对值函数
try:
    print(mwh_abs('10'))
except TypeError as e:
    # 如果发生异常，打印异常信息
    print("抛出了异常, msg:", e)

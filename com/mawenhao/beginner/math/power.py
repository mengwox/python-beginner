def power(x, n=2):
    """
    计算x的n次方
    :param x: x
    :param n: 几次方
    :return: x的n次方
    """
    res = 1
    while n > 0:
        n = n - 1
        res = res * x
    return res


def return_tuple():
    return [1, 2, 3]


def add_end(arr=None):
    if arr is None:
        arr = []
    arr.append('end')
    return arr


# 计算numbers集合内的数之和
def cal(*numbers):
    res = 0
    for x in numbers:
        res = res + x
    return res


# 创建一个对象:人
def person(name, age, **kwargs):
    print("姓名:%s" % name)
    print("年龄:%d" % age)
    if 'other' in kwargs:
        print("other:", kwargs['other'])

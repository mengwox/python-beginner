from functools import reduce


def is_palindrome_str(n):
    """
    转字符串,并使用高级特性:切片,完成回数筛选
    :param n:
    :return:
    """
    return str(n) == str(n)[::-1]


def is_palindrome(n):
    """
    判断n是否是回数
    :param n:
    :return:
    """
    if n < 10:
        return True
    else:
        res = []
        temp = n
        while temp > 0:
            res.append(temp % 10)
            temp = temp // 10
        total = reduce(lambda x, y: x * 10 + y, res)
        return total == n


# 测试:
output = filter(is_palindrome, range(1, 1000))
print()
print('1~1000:', list(output))
pre_res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
           101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
if list(filter(is_palindrome, range(1, 200))) == pre_res:
    print('测试成功!')
else:
    print('测试失败!')


def count():
    def f(i):
        def g():
            return i * i

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


print()
f = inc()
print(f())
print(f())

from collections.abc import Iterable
from functools import reduce


def add(x, y, f=abs):
    return f(x) + f(y)


print()
print(add(5, -12, abs))


def sqrt(x, n=2):
    res = x
    while n > 1:
        res = res * x
        n = n - 1
    return res


def do_map(li):
    if isinstance(li, Iterable):
        return list(map(sqrt, li))
    else:
        return []


print()
print(do_map([1, 2, 3, 4]))


def do_reduce(li):
    if isinstance(li, Iterable):
        return reduce(lambda x, y: abs(x) + abs(y), li)
    else:
        return []


print()
print(do_reduce([1, -3, -5, -10]))


def fn(x, y):
    return x * 10 + y


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    assert isinstance(s, str)
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print()
print(str2int('13579'))


def normalize(name):
    if isinstance(name, Iterable) and isinstance(name, str):
        return name[0].upper() + name[1:].lower()
    else:
        pass


print()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print()
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('prod函数测试成功!')
else:
    print('prod函数测试失败!')


def str2float(s):
    if not isinstance(s, str):
        pass
    else:
        sl = s.split('.')
        res1 = reduce(lambda x, y: x * 10 + y, map(char2num, sl[0]))
        res2 = reduce(lambda x, y: x * 10 + y, map(char2num, sl[1])) / sqrt(10, len(sl[1]))

        return res1 + res2


res = str2float('123.456')
if (res - 123.456) < 0.0000001:
    print("str2float函数,res:%f,测试成功!" % res)
else:
    print("str2float函数,res:%f,测试失败!" % res)

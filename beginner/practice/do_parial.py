# 偏函数使用
import functools


def binary2int(num_str, *bit):
    """
    num_str 二进制字符串转10进制数字
    :return: 10进制数字
    """
    func = functools.partial(int, base=2)
    try:
        if bit is not None and isinstance(bit, tuple) and len(bit) > 0:
            return func(num_str, base=bit[0])
        else:
            return func(num_str)
    except ValueError as e:
        print(num_str + "不是二进制字符串")
        print(f"error: {e}")


# 测试
print()
print(binary2int('10101'))

max_partial = functools.partial(max, 10)
print(max_partial(2, 5, 6))

import logging


# 高阶函数用法, 将函数作为入参
def process_range(start: int, end: int, func):
    """
    对从start到end范围内的每个数应用函数func。

    :param start: 起始值
    :param end: 结束值
    :param func: 应用于每个数的函数
    """
    result = 0
    if not callable(func):
        raise TypeError('func must be callable')
    for n in range(start, end + 1):
        try:
            result = result + func(n)
        except Exception as e:
            logging.error(f"异常类型: {type(e).__name__}, 异常信息: {e}")
            logging.exception(e)
            return
    print(f'from {start} to {end}, sum is {result}')


# 示例使用
def ele_func(n: int) -> int:
    return n * n + 1


print()
# 调用 process_range 函数
process_range(1, 100, ele_func)

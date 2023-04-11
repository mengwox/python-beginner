import functools
import time
from types import FunctionType, MethodType


def log(func):
    """
    装饰器,日志打印
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call %s()" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


def log_with_text(text):
    """
    装饰器,自定义日志打印
    :param text:
    :return:
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_with_text('execute')
def now():
    print('2023-04-10')


print()
now()


def metric(fn):
    """
    请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
    :param fn:
    :return:
    """

    @functools.wraps(fn)
    def decorator(*args, **kwargs):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args, **kwargs)

    return decorator


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


# 测试
f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def log_with_or_not_text(param):
    def decorator(func, text=param):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("func:%s log start" % func.__name__)
            if text is not None:
                print("text: %s" % text)
            res = func(*args, **kwargs)
            print("func:%s log end" % func.__name__)
            return res

        return wrapper

    if param is isinstance(param, (FunctionType, MethodType)) or hasattr(param, '__call__'):
        return decorator(param, None)
    decorator.text = param
    return decorator


@log_with_or_not_text
def nows():
    print('2023-04-10 mawenhao hello!')


print()
nows()

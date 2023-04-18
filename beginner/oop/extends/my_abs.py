class MyAbs(object):
    """
    Return abs of input num

    >>> myAbs = MyAbs()
    >>> myAbs.my_abs(10)
    10
    >>> myAbs.my_abs(-10)
    10
    >>> myAbs.my_abs(0)
    0
    """

    def my_abs(self, num: int) -> int:
        if num < 0:
            num = -num
        return abs(num)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

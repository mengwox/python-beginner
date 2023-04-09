def by_name(t):
    """
    按名字排序
    :param t:
    :return:
    """
    if not isinstance(t, tuple):
        raise '入参不是tuple类型'
    else:
        return t[0]


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_name)
# print()
# print(L2)


def by_score(t):
    """
    按成绩从高到低排序
    :param t:
    :return:
    """
    if not isinstance(t, tuple):
        raise '入参不是tuple类型'
    else:
        return -t[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_score)
print()
print(L2)

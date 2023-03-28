def find_min_max(array):
    """
    使用迭代查找一个list中最小和最大值，并返回一个tuple
    :param array:
    :return:
    """
    if array is None or array == []:
        return None, None
    min_ele = max_ele = 0
    for ele in array:
        if min_ele == 0 or min_ele > ele:
            min_ele = ele
        if max_ele == 0 or max_ele < ele:
            max_ele = ele
    return min_ele, max_ele

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    """
    利用切片操作，实现一个trim()函数
    :param s:
    :return:
    """
    if s is None:
        return None
    sln = len(s)
    if sln == 0:
        return ""
    elif sln == 1:
        if s == " ":
            return ""
        else:
            return s
    start = 0
    end = -1
    for c in s:
        if c == " ":
            if end == -1:
                start = start + 1
            else:
                end = end + 1
        else:
            end = 0
    return s[start: sln - end]

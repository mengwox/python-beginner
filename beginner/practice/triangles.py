def triangles():
    pass


def triangle(n):
    if n == 1:
        return [1, ]
    elif n == 2:
        return [1, 1]
    else:
        temp = triangle(n - 1)
        res = []
        pre = 0
        cur = 0
        for i, val in enumerate(temp):
            if i == 0:
                pre = 0
            else:
                pre = temp[i - 1]
            res.insert(i, pre + temp[i])
        res.insert(n, 1)
        return res

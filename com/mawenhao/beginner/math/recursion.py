# 循环方式 实现计算阶乘
def fact_while(n):
    res = n
    while n > 1:
        n = n - 1
        res = res * n
    return res


# 普通递归 实现计算阶乘,有栈溢出的问题
def fact_recursion(n):
    if n < 1:
        return 1
    return n * fact_recursion(n - 1)


# 尾递归 实现计算阶乘 python没有针对尾递归优化,所以还是有栈溢出的问题
def fact_tail(n, res=1):
    if n < 1:
        return res
    return fact_tail(n - 1, res * n)

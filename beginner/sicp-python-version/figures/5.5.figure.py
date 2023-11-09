def fib(n: int) -> int:
	if n <= 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


def factR(n: int) -> int:
	"""
	尾递归, 阶乘
	:param n: 大于0的整数
	:return: n的阶乘
	"""
	if n <= 1:
		return 1
	else:
		return n * factR(n - 1)


def applyToEach(L: list, f):
	for ele in range(len(L)):
		L[ele] = f(L[ele])


L = [1, -2, 3.33]
print('L =', L)
print('Apply abs to each element of L.')
applyToEach(L, abs)
print('L =', L)
print('Apply int to each element of', L)
applyToEach(L, int)
print('L =', L)
print('Apply factorial to each element of', L)
applyToEach(L, factR)
print('L =', L)
print('Apply Fibonnaci to each element of', L)
applyToEach(L, fib)
print('L =', L)

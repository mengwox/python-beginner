def factI(n: int) -> int:
	"""
	线性递归, 阶乘
	:param n: 大于0的整数
	:return: n的阶乘
	"""
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result


def factR(n: int) -> int:
	"""
	尾递归, 阶乘
	:param n: 大于0的整数
	:return: n的阶乘
	"""
	if n == 1:
		return 1
	else:
		return n * factR(n - 1)

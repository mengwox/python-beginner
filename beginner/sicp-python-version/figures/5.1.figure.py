def find_extreme_divisors(x: int, y: int) -> tuple:
	"""
	:param x: must be a positive int num
	:param y: must be a positive int num
	:return:a tuple, first is min divisor; second is max divisor
	"""
	min_divider = max_divider = None
	for ele in range(2, min(x, y) + 1):
		if x % ele == 0 and y % ele == 0:
			if min_divider is None:
				min_divider = ele
			max_divider = ele
	print('min is %d, max is %d' % (min_divider, max_divider))
	return min_divider, max_divider


# verify tuple is immutable
demo = (1, 2, 3)
print(demo)
demo1 = 4,
demo.__add__(demo1)
print(demo)

demo = 1,
print(demo)
print(type(demo))

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t1)
print(t2)
print(t1 + t2)
print((t1 + t2)[2:])
t2 = t1[:]
print(t1 == t2)
print(t1 == t1[::])
print(find_extreme_divisors(100, 200))
print(type(range(100)))
L = [1]
print(type(L))

# When the implementation of fib in Figure 4.7 is used to compute
# fib(5), how many times does it compute the value of fib(2) on the way to computing fib(5)?
COUNT = 0


def fib(n: int) -> int:
	print('fib(%d) enter' % n)
	if n == 2:
		global COUNT
		COUNT += 1
	if n <= 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


print(fib(5))
print(COUNT)

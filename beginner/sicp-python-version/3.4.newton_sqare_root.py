def not_good_enough(guess, epsilon, x) -> bool:
	return abs(x - guess ** 2) > epsilon


def improve(guess, x) -> float:
	return guess - (guess ** 2 - x) / (2 * guess)


# return (guess + x / guess) / 2.0


# newton method, to find out the square root of x
x = int(input('Enter a Number:'))
if x < 0:
	print('InValid Number.')
elif x == 0:
	print(0, 'is the square root of', x)
else:
	# guess = 1.0
	guess = x / 2.0
	numGuesses = 0
	epsilon = 0.000001
	while not_good_enough(guess, epsilon, x):
		numGuesses += 1
		print('x is', x, 'NumberGuesses:', numGuesses, 'guess is', guess)
		guess = improve(guess, x)
	print('Number Guess Count:', numGuesses)
	print(guess, 'is close to the square root of', x)

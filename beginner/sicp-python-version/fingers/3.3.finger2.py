# bisection method, to find out the cube root of x
x = int(input('Enter a positive or negative Number:'))
pos = abs(x)
epsilon = 0.000001
numGuesses = 0
low = 0.0
high = max(1.0, pos)
ans = (low + high) / 2.0
while abs(ans ** 3 - pos) >= epsilon:
	print('low =', low, ',high =', high, ' ans =', ans)
	numGuesses += 1
	if ans ** 3 < pos:
		low = ans
	else:
		high = ans
	ans = (low + high) / 2.0
print('numGuesses =', numGuesses)
if x < 0:
	ans = -ans
print(ans, 'is close to cube root of', x)

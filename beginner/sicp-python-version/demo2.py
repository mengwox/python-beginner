num = int(input('Enter a Integer: '))
root = 0
while root <= num:
	pwr = 1
	while pwr < 6:
		if root ** pwr == num:
			print('num is', num, '; root is', root, ',pwr is', pwr)
		pwr += 1
	root += 1
print('End!')

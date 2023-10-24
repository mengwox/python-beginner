numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
# concatenate X to toPrint numXs times
numXs = int(numXs)
while numXs > 0:
	toPrint = toPrint + 'X'
	numXs -= 1
print(toPrint)

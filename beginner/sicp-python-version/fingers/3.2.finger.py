# Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
# sum of the numbers in s.
s = input('Enter a string: ')
total = 0
for ele in s.split(','):
	total += float(ele)
print(total)

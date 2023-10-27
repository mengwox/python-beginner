count = 3
largest_odd = None
while count > 0:
	temp = int(input("input a number! rest %d times now\n" % count))
	if temp % 2 == 1:
		if largest_odd is None:
			largest_odd = temp
		elif largest_odd < temp:
			largest_odd = temp
	count -= 1
if largest_odd is not None:
	print("error!")
else:
	print("largest odd number is", largest_odd)

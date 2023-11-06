x = int(input("Enter a Integer:"))
ans = 0
for ans in range(0, abs(x) + 1):
	if ans ** 3 >= abs(x):
		break
if ans ** 3 == abs(x):
	if x < 0:
		ans = -ans
	print(x, "'s cube root is", ans)
else:
	print(x, "is not a perfect number")

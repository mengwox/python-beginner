# Write a function isIn that accepts two strings as arguments and
# returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operation in.


def isIn(a: str, b: str) -> bool:
	return a.find(b) != -1 or b.find(a) != -1


str1 = 'abc'
str2 = 'ab'
print(isIn(str1, str2))

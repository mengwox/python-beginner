def isPalindrome(s: str) -> bool:
	"""
	:param s: string
	:return: True if letters in s form a palindrome;
	False otherwise. Non-letters and capitalization are ignored.
	"""

	def toChar(s: str):
		"""
		:param s: string
		:return: chars of s
		"""
		s = s.lower()
		letters = ""
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				letters += c
		return letters

	def isPal(s: str) -> bool:
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and isPal(s[1:-1])

	return isPal(toChar(s))

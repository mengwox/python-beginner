# Autograder: Regular Expressions

import re


def count_sum(file_name: str):
	try:
		content = open(file_name)
		num_sum = 0
		for cur_line in content:
			cur_nums = re.findall('\\d+', cur_line)
			if len(cur_nums) > 0:
				for num in cur_nums:
					num_sum += int(num)
		return num_sum
	except FileNotFoundError:
		print("file not exist!")
		return None


result = count_sum('files/regex_sum_1866310.txt')
if result is not None:
	print(result)

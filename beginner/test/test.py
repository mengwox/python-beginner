import unittest
from collections.abc import Iterable

from beginner.math.hannota import hanoi_tower
from beginner.math.recursion import *
from beginner.practice.advanced_features import trim
from beginner.practice.find_min_max import find_min_max
from beginner.practice.list_comprehension import list_compre
from beginner.practice.triangles import triangle
from gpt.constants import OFFICIAL_API_FILE
from gpt.gpt_utils import get_api_key


class MyTestCase(unittest.TestCase):
	def test_get_api_key_from_file(self):
		api_key = get_api_key(OFFICIAL_API_FILE)
		self.assertIsNotNone(api_key, "api key shouldn't null")

	def test_list_compre(self):
		L2 = list_compre()
		print(L2)
		self.assertTrue(L2 == ['hello', 'world', 'apple'], '测试失败!')

	def test_triangle(self):
		"""

		:return:
		"""
		n = 1
		results = []
		while n <= 10:
			result = triangle(n)
			print(result)
			n = n + 1
			results.append(result)
		res: bool = results == [
			[1],
			[1, 1],
			[1, 2, 1],
			[1, 3, 3, 1],
			[1, 4, 6, 4, 1],
			[1, 5, 10, 10, 5, 1],
			[1, 6, 15, 20, 15, 6, 1],
			[1, 7, 21, 35, 35, 21, 7, 1],
			[1, 8, 28, 56, 70, 56, 28, 8, 1],
			[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
		]
		self.assertTrue(res, '测试失败!')

	def test_iter_dict(self):
		"""
		迭代dict
		:return:
		"""
		dit = {1: 2, 2: 3, 3: 4}
		if isinstance(dit, Iterable):
			# 迭代dict,带kv
			for k, v in dit.items():
				print("key:", k, ",value:", v)
			# 迭代dict,只带k
			for k in dit.keys():
				print("key:", k)
			# 迭代dict,只带v
			for v in dit.values():
				print("value:", v)
		else:
			self.assert_(False, "dit不是一个可迭代对象")

	def test_iter(self):
		"""
		熟悉迭代操作
		:return:
		"""
		L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
		if isinstance(L, Iterable):
			print("L是一个可迭代对象")
			index = 0
			# for...in迭代
			for ele in L:
				print("index:", index, "元素值为", ele)
				index = index + 1
			# 迭代,带下标
			for i, ele in enumerate(L):
				print("带下标迭代之i:", i, "元素值为", ele)
		else:
			self.assert_(False, "L不是一个可迭代对象")

	def test_split(self):
		"""
		熟悉切片操作, 可用于list/tuple/字符串, 只要是可迭代的对象
		:return:
		"""
		L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
		print(L[0:3])
		print(L[-3:0])
		print(L[1:2])
		print(L[::2])
		self.assertEqual(L[0:1], ['Michael', ], "测试未通过")

	def test_recursion(self):
		"""
		测试递归
		:return: OK表示测试通过
		"""
		n = 5
		# 存在递归异常, 可以使用循环或者尾递归解决异常
		self.assertEqual(fact_recursion(n), 120)
		# 循环方式
		self.assertEqual(fact_while(n), 120)
		# 尾递归
		self.assertEqual(fact_tail(n), 120)

	def test_hannota(self):
		"""
		测试汉诺塔
		:return:
		"""
		print(hanoi_tower(3, 'A', 'B', 'C'))

	def test_trims(self):
		"""
		测试字符串首尾去空串
		:return:
		"""
		if trim('hello  ') != 'hello':
			print('测试失败!')
		elif trim('  hello') != 'hello':
			print('测试失败!')
		elif trim('  hello  ') != 'hello':
			print('测试失败!')
		elif trim('  hello  world  ') != 'hello  world':
			print('测试失败!')
		elif trim('') != '':
			print('测试失败!')
		elif trim('    ') != '':
			print('测试失败!')
		else:
			print('测试成功!')

	def test_find_min_max(self):
		"""
		使用迭代查找一个list中最小和最大值，并返回一个tuple
		单元测试
		:return:
		"""
		if find_min_max([]) != (None, None):
			print('测试失败!')
		elif find_min_max([7]) != (7, 7):
			print('测试失败!')
		elif find_min_max([7, 1]) != (1, 7):
			print('测试失败!')
		elif find_min_max([7, 1, 3, 9, 5]) != (1, 9):
			print('测试失败!')
		else:
			print('测试成功!')


if __name__ == '__main__':
	unittest.main()

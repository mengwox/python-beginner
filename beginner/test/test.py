import unittest
from collections.abc import Iterable

from beginner.math.hannota import hanoi_tower
from beginner.math.recursion import *
from beginner.practice.advanced_features import trim
from beginner.practice.find_min_max import find_min_max


class MyTestCase(unittest.TestCase):
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

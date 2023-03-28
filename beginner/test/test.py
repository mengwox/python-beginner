import unittest

from beginner.math.hannota import hanoi_tower
from beginner.math.recursion import *
from beginner.practice.advanced_features import trim


class MyTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()

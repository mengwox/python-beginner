import unittest

from com.mawenhao.beginner.math.hannota import hanoi_tower
from com.mawenhao.beginner.math.recursion import *


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

if __name__ == '__main__':
    unittest.main()

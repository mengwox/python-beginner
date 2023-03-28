# 汉诺塔
# 移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法，例如：
# todo 有待理解动态规划问题
def hanoi_tower(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return None
    hanoi_tower(n - 1, a, c, b)
    hanoi_tower(1, a, b, c)
    hanoi_tower(n - 1, b, a, c)

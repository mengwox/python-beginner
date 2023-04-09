def create_counter():
    x = 0

    def counter():
        nonlocal x
        x = x + 1
        return x

    return counter


# 测试:
counterA = create_counter()
print()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)

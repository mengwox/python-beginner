import traceback


# 编写一个名为 collatz()的函数，它有一个名为 number 的参数。如果参数是偶数，那么 collatz()就打印出 number // 2，并返回该值。如果 number 是奇数，collatz()就打印并返回 3 *
# number + 1。 然后编写一个程序，让用户输入一个整数，并不断对这个数调用 collatz()，直到函数返回值１（令人惊奇的是，这个序列对于任何整数都有效，利用这个序列，你迟早会得到
# 1！既使数学家也不能确定为什么。你的程序在研究所谓的“Collatz 序列”，它有时候被称为“最简单的、不可能的数学问题”）。
def collatz(number: int):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


def return_void() -> None:
    pass


def invoke_collatz() -> None:
    goal = 1
    times = 0
    input_str = input("please input a Integer:\n")
    try:
        input_int = int(input_str)
    except ValueError:
        print(traceback.format_exc())
        print(f"Invalid Integer: {input_str}")
        return
    while True:
        if input_int == goal:
            print(f"end! got the goal: {goal}")
            break
        else:
            times = times + 1
            print(f"times: {times: > 5}, before: {input_int: > 5}, after: {collatz(input_int): > 5}")
            input_int = collatz(input_int)
    print(times)


def eggs(arr: list):
    arr.append('eggs')


if __name__ == '__main__':
    # invoke_collatz()
    # print(return_void())
    dic = {'abc': 'a', 'bc': 'b', 123: 2}
    dic['abc'] = 'b'
    print(dic)
    print('fwfew' in dic)

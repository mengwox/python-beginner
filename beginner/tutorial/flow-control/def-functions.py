# Defining Functions
# 斐波那契数列
def fib(n):
    """
    Print a Fibonacci series up.
    :param n: print util large or equals n
    :return: None
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)
f = fib
print("function named f start")
f(1000)
print(f(0))


def fib2(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fib2(1000))


# More on Defining Functions
def ask_ok(prompt, reties=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye,', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        reties = reties - 1
        if reties < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok('Do you really want to quit')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

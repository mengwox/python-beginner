def _odd_iter():
    odd = 1
    while True:
        odd = odd + 2
        yield odd


def _not_divisible(div_num):
    return lambda x: x % div_num > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        prime_num = next(it)
        yield prime_num
        it = filter(_not_divisible(prime_num), it)


print()
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

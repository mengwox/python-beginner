# `break` and `continue` Statements
# and `else` Clauses on Loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            # 6//2 = 3, 6/2 = 3.0
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # 这里,只有在for迭代结束后,且未被break才会执行
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number:', num)
        continue
    print('Found an odd number:', num)

# range() Function

print("The range() Function==========================")
for i in range(5):
    print(i)

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

# 使用rang() + len(),实现序列按索引迭代
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# 但是, 使用enumerate()函数更加方便
for s in enumerate(a, 0):
    print(s)
    print(isinstance(s, tuple))

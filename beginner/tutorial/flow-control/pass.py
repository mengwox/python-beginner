# pass Statements
# 用处1:
# while True:
#     pass


# 用处2: 构建最小class
class MyEmptyClass:
    pass


print(MyEmptyClass())


# 用处3: 作为占位符,用作function函数或条件语句的body内容
def initlog(*args):
    pass


initlog()

# 3.11 Python Tutorial, 4:More Control Flow Tools
# if Statements
def abs_num(x):
    if x < 0:
        return -x
    elif x == 0:
        return x
    else:
        return x


print("if Statements==========================")
print(abs_num(-10))
print(abs_num(0))
print(abs_num(10))

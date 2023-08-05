# 3.11 Python Tutorial, 4:More Control Flow Tools
def abs_num(x):
    if x < 0:
        return -x
    elif x == 0:
        return x
    else:
        return x


print(abs_num(-10))
print(abs_num(0))
print(abs_num(10))


def http_error(http_status: int):
    match http_status:
        case 200:
            print("http status is 200 ok")
        case 400:
            print("http status is 400 valid error")
        case 500:
            print("http status is 500 system error")
        case _:
            print("unknown http status! status: %d" % http_status)


status = 200
http_error(status)
status = 400
http_error(status)
status = 500
http_error(status)
status = 404
http_error(status)


def pointer(pointer_point):
    match pointer_point:
        case (0, 0):
            print('Origin')
        case (x, 0):
            print(f'X={x}')
        case (0, y):
            print(f'Y={y}')
        case (x, y):
            print(f'X={x}, Y={y}')
        case _:
            raise ValueError('Not a point')


point = 1
try:
    pointer(point)
except ValueError as ve:
    print(ve.args[0])
point = (0, 0)
pointer(point)
point = (0, 1)
pointer(point)
point = (1, 0)
pointer(point)
point = (1, 2)
pointer(point)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(pointObj: Point):
    match pointObj:
        case Point(x=0, y=0):
            print('Origin')
        case Point(x=x, y=0):
            print(f'X={x}')
        case Point(x=0, y=y):
            print(f'Y={y}')
        case Point(x=x, y=y):
            print(f'X={x}, Y={y}')
        case _:
            raise ValueError('Not a point')


print("match by class Point start ==================")
point = Point(0, 0)
where_is(point)
point = Point(0, 1)
where_is(point)
point = Point(1, 0)
where_is(point)
point = Point(1, 2)
where_is(point)
point = 1
try:
    # noinspection PyTypeChecker
    where_is(point)
except ValueError as ve:
    print(ve.args[0])

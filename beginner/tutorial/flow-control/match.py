# match Statements
from enum import Enum


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


print("match Statements==========================")
status = 200
http_error(status)
status = 400
http_error(status)
status = 500
http_error(status)
status = 404
http_error(status)


def pointer(pointer_point: tuple):
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
    # noinspection PyTypeChecker
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
    __match_args__ = ('x', 'y')

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

points = [Point(0, 2), Point(0, 1)]
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")


def match_if(point: Point):
    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
match color:
    case Color.RED:
        print('I see red!')
    case Color.GREEN:
        print('Grass is green')
    case Color.BLUE:
        print("I'm feeling the blues :(")

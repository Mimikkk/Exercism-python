from itertools import combinations
from functools import reduce
from typing import *

class Point(object):
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

def rectangles(data: List[str]):
    def is_safe(i: int, j: int) -> bool:
        return size_x > i >= 0 and size_y > j >= 0

    def is_rectangle_connection(points: Iterable[Point]) -> bool:
        (a, b, c, d) = points
        if (a.x == b.x and c.x == d.x) and (a.y == c.y and b.y == d.y):
            # Check horizontal connection between a and b
            y = a.y+1
            while y != b.y:
                if is_safe(a.x, y) and data[a.x][y] in '-+': y += 1
                else: return False

            # Check vertical connection between a and c
            x = a.x+1
            while x != c.x:
                if is_safe(x, a.y) and data[x][a.y] in '|+': x += 1
                else: return False

            # Check horizontal connection between c and d
            y = c.y+1
            while y != d.y:
                if is_safe(c.x, y) and data[c.x][y] in '-+': y += 1
                else: return False

            # Check vertical connection between b and d
            x = b.x+1
            while x != d.x:
                if is_safe(x, b.y) and data[x][b.y] in '|+': x += 1
                else: return False
            return True
        return False

    def is_rectangle_math(points: Iterable[Point]) -> bool:
        sum_x, sum_y = map(lambda x: x / 4, reduce(lambda sum_, p: (sum_[0] + p.x, sum_[1] + p.y), points, (0, 0)))
        return len(set(map(lambda p: (p.x - sum_x) ** 2 + (p.y - sum_y) ** 2, points))) <= 1

    def is_rectangle(points: Iterable[Point]) -> bool:
        return is_rectangle_math(points) and is_rectangle_connection(points)

    if not data: return 0
    size_x = len(data)
    size_y = len(data[0])

    return sum(map(is_rectangle, combinations(
        (Point(x, y) for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == '+'), r=4)))

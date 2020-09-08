from typing import *


class Point(object):
    def __init__(self, x: int, y: int, val: str = None):
        self.x = x
        self.y = y
        self.val = val

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Point({self.x}, {self.y}: {self.val})'


class WordSearch(object):
    def __init__(self, puzzle: List[str]):
        if not puzzle: raise ValueError('No Puzzle')
        self.size = Point(len(puzzle), len(puzzle[0]))
        self.data = [[Point(x, y, puzzle[x][y]) for y in range(self.size.y)] for x in range(self.size.x)]

    def search(self, word: str):
        result: List[Point] = []
        for (start_point, (m, n), end_point) in self.find_potential(len(word)):
            cur_word: str = ''
            point = start_point
            while point != end_point:
                cur_word += point.val
                point = self.data[point.x+m][point.y+n]
            cur_word += point.val
            if cur_word == word or cur_word[::-1] == word:
                result.append(Point(start_point.y, start_point.x))
        return tuple(result)

    def is_safe(self, i: int, j: int) -> bool:
        return self.size.x > i >= 0 and self.size.y > j >= 0

    def find_potential(self, len_: int) -> Tuple[Point, Tuple[int, int], Point]:
        yield from ((self.data[x][y], (m, n), self.data[i][j])
                    for x in range(self.size.x) for y in range(self.size.y)
                    for (m, n) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    if self.is_safe((i := x + (len_ - 1) * m), (j := y + (len_ - 1) * n)))

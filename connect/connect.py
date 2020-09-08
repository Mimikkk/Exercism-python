from collections import deque
from typing import *

class Point(object):
    def __init__(self, x: int, y: int, val: chr = ''):
        self.x: int = x
        self.y: int = y
        self.val: chr = val

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return f'Point({self.x}, {self.y}: {self.val})'

class ConnectGame(object):

    def __init__(self, board):
        if not (board := board.replace(' ', '').split('\n')): raise ValueError("Empty Board")
        self.size: Point = Point(len(board), len(board[0]))

        self.board: Tuple[Tuple[Point]] = tuple(
            tuple(Point(x, y, board[x][y]) for y in range(self.size.y)) for x in range(self.size.x))
        self.trans: Tuple[Tuple[Point]] = tuple(zip(*self.board))

    def get_winner(self):
        return ('', 'O' if (winner_o := self.is_winner('O')) else 'X', '')[winner_o + self.is_winner('X')]

    def is_winner(self, player):
        stack = deque(filter(lambda p: p.val == player, (self.trans[0] if player == 'X' else self.board[0])))

        visited: Set[Point] = set()
        while stack:
            visited.add(point := stack.pop())

            if self.is_finished(point, player): return True
            stack.extend(p for p in self.neighbors(point) if p not in visited and p.val == player)
        return False

    def is_finished(self, p: Point, player: chr) -> bool:
        return p.y == self.size.y - 1 if player == 'X' else p.x == self.size.x - 1

    def is_safe(self, i: int, j: int) -> bool:
        return self.size.x > i >= 0 and self.size.y > j >= 0

    def neighbors(self, p: Point) -> Iterable[Point]:
        yield from (self.board[x][y]
                    for (m, n) in [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
                    if self.is_safe((x := p.x+m), (y := p.y+n)))

from typing import *


class Queen(object):
    def __init__(self, row: int, column: int):
        self.size: int = 8
        if not self.is_safe(row, column): raise ValueError('Queen is off the board')

        self.row: int = row
        self.column: int = column
        self.moves: Tuple[Tuple[int, int], ...] = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    def is_safe(self, i, j) -> bool:
        return self.size > i >= 0 and self.size > j >= 0

    def can_attack(self, other: 'Queen') -> bool:
        if (self.row, self.column) == (other.row, other.column): raise ValueError('Queen are on the same tile')

        for (m, n) in self.moves:
            (i, j) = self.row - m, self.column - n
            while self.is_safe(i := i + m, j := j + n):
                if (i, j) == (other.row, other.column): return True
        return False

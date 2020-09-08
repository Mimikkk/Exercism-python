from typing import *
import re


def annotate(minefield: List[str]) -> List[str]:
    if not minefield: return []
    len_x = len(minefield)
    len_y = len(minefield[0])

    if any(re.search(r'[^* ]', row) or len(row) != len_y for row in minefield):
        raise ValueError('Bad Input Matrix')

    def is_safe(i: int, j: int) -> bool:
        return len_x > i >= 0 and len_y > j >= 0

    minefield: List[List[chr]] = list(map(list, minefield))
    neigh: List[Tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for x in range(len_x):
        for y in range(len_y):
            if minefield[x][y] != '*':
                minefield[x][y] = (str(v)
                                   if (v := sum(is_safe(x + m, y + n) and minefield[x + m][y + n] == '*'
                                                for (m, n) in neigh)) else ' ')
    return list(map(''.join, minefield))

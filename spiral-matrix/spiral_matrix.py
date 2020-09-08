from typing import *


def spiral_matrix(size: int) -> List[List[int]]:
    def is_safe(i: int, j: int):
        return size > i >= 0 and size > j >= 0 and result[i][j] == -1

    result: List[List[int]] = [[-1] * size for _ in range(size)]

    x: int = 0
    y: int = -1
    value: int = 0
    direction: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for (m, n) in map(lambda turn: direction[turn % 4], range(size**2)):
        while is_safe(x + m, y + n):
            result[(x := x + m)][(y := y + n)] = (value := value+1)
    return result

from typing import *
def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    len_x: int = 0
    len_y: int = 0
    if (len_x := len(matrix)) == 0 or (len_y := len(matrix[0])) == 0:
        return []

    if any(len_y != len(matrix[i]) for i in range(1, len_x)):
        raise ValueError("Irregular Matrix : Rawr xD")

    min_rows: List[int] = [max(row) for row in matrix]
    max_cols: List[int] = [min(col) for col in zip(*matrix)]

    return [
        {'row': x, 'column': y}
        for (x, x_val) in enumerate(min_rows, 1)
        for (y, y_val) in enumerate(max_cols, 1)
        if matrix[x-1][y-1] == x_val == y_val]

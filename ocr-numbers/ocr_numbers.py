from typing import *

dict_: Dict[str, str] = {' _ | ||_|   ': '0',
                         '     |  |   ': '1',
                         ' _  _||_    ': '2',
                         ' _  _| _|   ': '3',
                         '   |_|  |   ': '4',
                         ' _ |_  _|   ': '5',
                         ' _ |_ |_|   ': '6',
                         ' _   |  |   ': '7',
                         ' _ |_||_|   ': '8',
                         ' _ |_| _|   ': '9'}


def convert(grid: List[str]) -> str:
    if not grid or len(grid) % 4 != 0: raise ValueError('lines not multiple of 4')
    if len(grid[0]) % 3 != 0: raise ValueError('columns not multiple of 3')

    return ','.join(
                ''.join(
                    map(lambda x: dict_.get(''.join(x), '?'),
                        zip(*[[l[i:i + 3] for i in range(0, len(l), 3)] for l in grid[k:k + 4]])))
                for k in range(0, len(grid), 4))

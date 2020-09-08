from functools import reduce
from collections import deque
from typing import *

def product(list_: Deque[int]) -> int:
    return reduce(lambda x, y: x*y, list_, 1)

def largest_product(series: str, size: int) -> int:
    if not series and not size: return 1
    if not size: return 1

    if not series.isdigit(): raise ValueError('Alphabet Rawr xD')
    if not series and size > 0: raise ValueError('Span Rawr xD')
    if size > len(series): raise ValueError('Too big span Rawr xD')
    if size < 0: raise ValueError('Negative span Rawr xD')
    
    series_iter: Iter[int] = iter(map(int, series))
    curr: Deque[int] = deque(next(series_iter) for _ in range(size))

    max_: int = product(curr)
    while (next_ := next(series_iter, None)) is not None:
        curr.append(next_)
        curr.popleft()
        max_ = max(max_, product(curr))
    return max_

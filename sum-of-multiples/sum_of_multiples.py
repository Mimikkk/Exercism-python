from typing import *

def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    if not multiples: return 0
    if 0 in multiples: multiples.remove(0)

    return sum(n for n in range(limit) if any(n % p == 0 for p in multiples))

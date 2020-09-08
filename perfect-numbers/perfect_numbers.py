from typing import *


def find_factors(n: int) -> Tuple[int]:
    return tuple(i for i in range(1, n//2+1) if n % i == 0)


def classify(n: int) -> str:
    if n <= 0: raise ValueError('Rawr xD')
    return ["deficient", "perfect", "abundant"][((sum_ := sum(find_factors(n))) > n) + (sum_ >= n)]

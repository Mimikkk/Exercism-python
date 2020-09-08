from typing import *
from math import sqrt


def triplets_with_sum(n: int) -> List[List[int]]:
    triplets: List[List[int]] = []

    a: int = 1
    m: int = int(n * (1 - sqrt(2) / 2))
    max_: int = ((2 * n * m - n ** 2) / (2 * (m - n)))
    while a < max_:
        b: int = int((2 * n * a - n ** 2) / (2 * (a - n)))
        c: int = n - (a + b)
        if is_triplet(triplet := [a, b, c]): triplets.append(triplet)
        a += 1
    return triplets


def triplets_in_range(start: int, end: int) -> List[List[int]]:
    return list(*map(triplets_with_sum, range(start, end)))


def is_triplet(triplet: List[int]) -> bool:
    a, b, c = triplet
    return a ** 2 + b ** 2 == c ** 2

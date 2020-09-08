from typing import *


def primes(n: int) -> List[int]:
    if n <= 1: return []
    primes: List[int] = [2]
    [primes.append(num) for num in range(3, n + 1, 2) if not any(num % p == 0 for p in primes)]
    return primes

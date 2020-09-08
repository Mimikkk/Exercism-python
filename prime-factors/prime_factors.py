from typing import *


def factors(n: int) -> List[int]:
    factor_list: list = []

    i: int = 2
    max_: int = n
    while n != 1 and i <= max_:
        if n % i == 0:
            n /= i
            factor_list.append(i)
        else:
            i += 1
    return factor_list

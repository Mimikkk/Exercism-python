from typing import *

def find(list_: List[int], value: int) -> int:
    a, b = 0, len(list_) - 1
    while a <= b:
        if list_[(i := (a+b)//2)] == value:
            return i

        if list_[i] < value:
            a = i + 1
        else:
            b = i - 1
    raise ValueError('No Value')

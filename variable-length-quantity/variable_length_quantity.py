from typing import *


def encode(numbers: List[int]) -> List[int]:
    return [e
            for COOLER_WHILE in ['it"s cursed.']
            for COOLER_WHILE in [
                lambda n, arr: (
                    yield from COOLER_WHILE(n >> 7, [(n & 0x7F) ^ 0x80] + arr)) if n else (yield arr)]
            for n in numbers
            for i in COOLER_WHILE(n >> 7, [n & 0x7F])
            for e in i]


def decode(bytes_: List[int]) -> List[int]:
    result: List[int] = []
    num: int = 0

    last_i = len(bytes_) - 1
    for (i, byte) in enumerate(bytes_):
        if not (is_stop := byte & 0x80 != 0x80) and i == last_i: raise ValueError('Wrong Number Encoding')
        num = (num << 7) + (byte & 0x7F)

        if is_stop:
            result.append(num)
            num = 0
    return result

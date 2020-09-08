from typing import *

numbers_1_12: Dict[int, str] = {0: "",
                                1: "one",
                                2: "two",
                                3: "three",
                                4: "four",
                                5: "five",
                                6: "six",
                                7: "seven",
                                8: "eight",
                                9: "nine",
                                10: "ten",
                                11: "eleven",
                                12: "twelve"}
numbers_multipliers: Dict[int, str] = {0: "",
                                       1: "teen",
                                       2: "twenty",
                                       3: "thirty",
                                       4: "forty",
                                       5: "fifty",
                                       6: "sixty",
                                       7: "seventy",
                                       8: "eighty",
                                       9: "ninety",
                                       10: "hundred",
                                       11: "thousand",
                                       12: "million",
                                       13: "billion"}


def handle_1_99(chunk: int) -> str:
    if chunk <= 12: return numbers_1_12[chunk]
    if chunk <= 99: return (f'{numbers_1_12[chunk % 10]}{numbers_multipliers[1]}'
                            if chunk // 10 == 1
                            else f'{numbers_multipliers[chunk // 10]}'
                                 f'{(f"-{numbers_1_12[chunk % 10]}" if chunk % 10 != 0 else "")}')

def handle_100s(chunk: int) -> str:
    return ((f'{numbers_1_12[chunk // 100]} {numbers_multipliers[10]}' if chunk > 99 else '')
            + (' ' if chunk > 99 and chunk % 100 != 0 else '') + handle_1_99(chunk % 100))


def split_into_chunks(n: int) -> Iterator[int]:
    return iter(int(str_[max(0, i - 3):i]) for str_ in [str(n)] for i in range(len(str_), 0, -3))


def join_chunks(chunks: Iterator[str]):
    result: List[str] = []
    size: int = 10
    while (n := next(chunks, None)) is not None:
        result += [f'{n}{f" {numbers_multipliers[size]}" if n and size>10 else ""}']
        size += 1
    return ' '.join(reversed(result)).strip() if result[-1] else 'zero'

def say(n: int) -> str:
    if n < 0 or n >= 1000000000000: raise ValueError('Out of bounds Rawr xD')
    return join_chunks(map(handle_100s, split_into_chunks(n)))

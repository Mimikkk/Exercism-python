from itertools import zip_longest
from typing import *

def encode(message: str, rails: int) -> str:
    words: List[str] = []
    len_full: int = max(1, (rails - 1) * 2)
    len_half: int = len_full//2

    i: int
    for i in range(len_full):
        if len_full > i > len_half:
            words[len_half-i-1] = ''.join(map(
                ''.join, zip_longest(words[len_half-i-1], message[i::len_full], fillvalue='')))
        else:
            words += [message[i::len_full]]
    return ''.join(words)

def decode(encoded_message: str, rails: int) -> str:
    lengths = []
    len_ = len(encoded_message)

    len_full: int = max(1, (rails - 1) * 2)
    len_half: int = len_full//2

    for i in range(len_full):
        if len_full > i > len_half:
            lengths[len_half - i - 1] += len(range(i, len_, len_full))
        else:
            lengths += [len(range(i, len_, len_full))]
    letters = [iter(list(next(iter_) for _ in range(count))) for iter_ in [iter(encoded_message)] for count in lengths]

    i: int = 0
    is_rising: bool = False
    decoded_message: str = ''
    while chr_ := next(letters[i], None):
        decoded_message += chr_
        if (i := i+(-1 if is_rising else 1)) in [0, rails - 1]: is_rising = not is_rising

    return decoded_message

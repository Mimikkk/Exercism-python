from typing import *
import re

class Luhn(object):
    def __init__(self, card_num: str):
        self.card_num: str = card_num

    def valid(self) -> bool:
        if not (str_ := re.sub(' ', '', self.card_num)).isdigit() or str_ in '0': return False
        return sum(((d*2 if i % 2 else d) % 10) + ((d*2 if i % 2 else d) // 10)
                   for (i, d) in enumerate(map(int, reversed(str_)))) % 10 == 0


from typing import *


def rows(letter: str) -> List[str]:
    return ((words := [(str_ := f'{f"{chr(65 + i):>{len_ - i}}":<{len_}}') + str_[len_ - 2::-1]
                       for i in range(len_)]) + words[len_ - 2::-1]
            if (len_ := ord(letter.upper()) - 65 + 1) != 1
            else ['A'])

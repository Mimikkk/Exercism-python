from math import ceil, sqrt
from typing import *
import re

def cipher_text(plain_text: str):
    text: str = re.sub(r'[^\w]', '', plain_text.lower())
    len_: int = len(text)

    len_c: int = ceil(sqrt(len_))
    len_r: int = round(sqrt(len_))
    return ' '.join(t[i::len_c] for t in [f'{text:<{len_c*len_r}}'] for i in range(len_c))

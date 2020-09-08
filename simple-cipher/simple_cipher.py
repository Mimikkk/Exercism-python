from string import ascii_lowercase as ALPHA
from itertools import cycle
from random import sample
from typing import *

class Cipher(object):
    def __init__(self, key: Optional[str] = None):
        if key is None: self.key = ''.join(sample(ALPHA, len(ALPHA)))
        else: self.key = key

    def encode(self, text: str) -> str:
        return ''.join(ALPHA[((ord(c) + ord(k)) % 97) % 26] for c, k in zip(text, cycle(self.key)))

    def decode(self, text: str) -> str:
        return ''.join(ALPHA[ord(c) - ord(k)] for c, k in zip(text, cycle(self.key)))

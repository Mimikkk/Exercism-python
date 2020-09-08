import re


def decode(str_: str) -> str:
    return ''.join(chr_ * (int(len_) if len_ else 1)
                   for (len_, chr_) in map(lambda x:
                                           re.split(r'(?=[a-zA-Z\s])', x),
                                           re.findall(r'\d*[A-Za-z\s]', str_)))

def encode(str_: str) -> str:
    return ''.join(len_ + chr_
                   for (chr_, len_) in map(lambda x: (x[0], str(len(x)) if len(x) != 1 else ''),
                                           map(lambda m: m.group(), re.finditer(r'(.)\1*', str_))))

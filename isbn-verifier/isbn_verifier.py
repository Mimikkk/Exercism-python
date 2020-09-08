import re
def is_valid(isbn: str) -> bool:
    digits: list = re.findall(r'\d|X$', isbn)
    len_: int = len(digits)
    if len_ != 10: return False
    return sum(i * int(e) if e != 'X' else 10 for i, e in zip(range(10, 0, -1), digits)) % 11 == 0

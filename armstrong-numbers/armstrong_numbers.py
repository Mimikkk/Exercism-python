def is_armstrong_number(n: int) -> bool:
    str_: str = str(n)
    power: int = len(str_)
    return n == sum(map(lambda x: int(x)**power, str_))

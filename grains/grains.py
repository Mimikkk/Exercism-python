def square(n: int) -> int:
    if n <= 0 or n > 64: raise ValueError('Wrong n')
    return 2 ** (n-1)


def total() -> int:
    return 18446744073709551615

from functools import reduce


def square_of_sum(n: int) -> int:
    return reduce(lambda x, y: x + y, range(1, n + 1), 0)**2


def sum_of_squares(n: int) -> int:
    return reduce(lambda x, y: x + y**2, range(1, n + 1), 0)


def difference_of_squares(n: int) -> int:
    return square_of_sum(n)-sum_of_squares(n)

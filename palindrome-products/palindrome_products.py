from functools import reduce


def are_factors_valid(func):
    def inner(min_factor, max_factor):
        if min_factor > max_factor: raise ValueError('Rawr xD')
        return func(min_factor, max_factor)
    return inner

def is_palindrome(n: int) -> bool:
    return (str_ := str(n)) == str_[::-1]

@are_factors_valid
def largest(min_factor: int, max_factor: int):
    return determine_palindrome(min_factor, max_factor, is_smallest=False)


@are_factors_valid
def smallest(min_factor: int, max_factor: int):
    return determine_palindrome(min_factor, max_factor, is_smallest=True)


def determine_palindrome(min_factor: int, max_factor: int, is_smallest: bool):
    range_ = range(min_factor ** 2, max_factor ** 2 + 1)
    for num in (range_ if is_smallest else reversed(range_)):
        if is_palindrome(num) and any(min_factor <= num // factor <= max_factor
                                      for factor in range(min_factor, max_factor + 1)
                                      if not num % factor):
            return num, ((i, num // i)
                         for i in range(min_factor, max_factor + 1)
                         if num % i == 0 and min_factor <= i <= num // i <= max_factor)
    return None, []

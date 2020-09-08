from typing import *


def is_triangle(sides: List[int]) -> bool:
    a, b, c = sorted(sides)
    return a + b >= c and (a != 0 or b != 0 or c != 0)


def equilateral(sides: List[int]) -> bool:
    a, b, c = sides
    return is_triangle(sides) and a == b == c


def isosceles(sides: List[int]) -> bool:
    a, b, c = sides
    return is_triangle(sides) and (a == b or b == c or a == c)


def scalene(sides: List[int]) -> bool:
    a, b, c = sides
    return is_triangle(sides) and a != b != c

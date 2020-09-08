from math import sqrt

def score(x: int, y: int) -> int:
    if (distance_from_centroid := x ** 2 + y ** 2) <= 1:
        return 10
    elif distance_from_centroid <= 25:
        return 5
    elif distance_from_centroid <= 100:
        return 1
    return 0

from typing import *
def latest(scores: List[int]) -> int:
    return scores[-1] if scores else -1


def personal_best(scores: List[int]) -> int:
    return max(scores)


def personal_top_three(scores: List[int]) -> List[int]:
    return sorted(scores, reverse=True)[:3]

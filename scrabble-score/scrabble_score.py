from typing import *
def score(word: str) -> int:
    score_dict: Dict[str, int] = {
        'AEIOULNRST': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10
    }
    result: int = 0
    for e in word.upper():
        for key in score_dict:
            if e in key:
                result += score_dict[key]
                break
    return result

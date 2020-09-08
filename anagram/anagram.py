from typing import *


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    def is_anagram(str_: str) -> bool:
        return main_key == sorted(str_ := str_.lower()) and word.lower() != str_
    main_key: List[chr] = sorted(word.lower())

    return [candidate for candidate in candidates if is_anagram(candidate)]

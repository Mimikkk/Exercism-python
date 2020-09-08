from collections import defaultdict
from typing import *
import re
def count_words(sentence: str) -> DefaultDict[str, int]:
    result: DefaultDict = DefaultDict(int)
    for e in re.findall(r"[a-z0-9']+", sentence.lower()):
        result[e.strip("'")]+=1

    return result

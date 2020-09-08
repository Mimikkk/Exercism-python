from collections import defaultdict
from functools import reduce
from typing import *

class School(object):
    def __init__(self):
        self.__grades: DefaultDict[int, List[str]] = DefaultDict(list)

    def add_student(self, name: str, grade: int):
        self.__grades[grade].append(name)

    def roster(self) -> List[str]:
        return reduce(lambda x, y: x + y,
                      [sorted(item)
                       for (key, item) in sorted(
                          self.__grades.items()
                          , key=lambda x: x[0])
                       ], [])

    def grade(self, grade: int) -> List[str]:
        return sorted(self.__grades[grade])

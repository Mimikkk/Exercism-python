from typing import *
class Matrix:
    def __init__(self, matrix_str: str):
        self.__rows: List[List[int]] = \
            list(map(lambda x: list(map(int, x.split())), matrix_str.split('\n')))
        self.__columns: List[List[int]] = \
            list(map(list, zip(*self.__rows)))

    def row(self, i: int) -> List[int]:
        return self.__rows[i-1] if self.__rows else []

    def column(self, i: int) -> List[int]:
        return self.__columns[i-1] if self.__columns else []

from typing import *


def append(list1, list2) -> List[Any]:
    return concat((list1, list2))


def concat(lists) -> List[Any]:
    return [ele for list_ in lists for ele in list_]


def filter(function, list_) -> Iterable[Any]:
    return [ele for ele in list_ if function(ele)]


def length(list_) -> int:
    return sum(1 for _ in list_)


def map(function, list_) -> Iterable[Any]:
    return [function(ele) for ele in list_]


def foldl(function, list_, initial):
    for ele in list_:
        initial = function(initial, ele)
    return initial

def foldr(function, list_, initial):
    for ele in reverse(list_):
        initial = function(ele, initial)
    return initial

def reverse(list_):
    return [list_[i] for i in range(length(list_) - 1, -1, -1)]

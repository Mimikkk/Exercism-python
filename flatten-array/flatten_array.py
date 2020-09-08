from typing import *

def flatten(iterable: Iterable) -> Iterable:
    return list(flatten_iteratively(iterable))

def flatten_iteratively(nested_list: Iterable):
    while nested_list:
        if isinstance(sublist := nested_list.pop(0), list):
            nested_list = sublist + nested_list
        elif isinstance(sublist, int):
            yield sublist

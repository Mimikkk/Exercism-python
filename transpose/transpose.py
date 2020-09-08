from itertools import zip_longest
def transpose(str_: str) -> str:
    return '\n'.join(
        ''.join(arr).rstrip('*') for arr in zip_longest(*str_.split("\n"),
                                                        fillvalue='*')).replace("*", " ")
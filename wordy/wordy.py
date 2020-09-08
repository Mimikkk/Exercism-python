from functools import reduce
import re


def answer(sentence: str) -> int:
    if not (numbers := re.sub(' by', '_by', sentence).strip('?').split()[2:]):
        raise ValueError('Wrong sentence.')
    if (len(numbers) - 1) % 2 != 0:
        raise ValueError('Wrong number of arguments.')

    trans_dict: Dict[str, str] = {'plus': '+', 'minus': '-', 'divided_by': '/', 'multiplied_by': '*'}
    try:
        iter_ = map(lambda word:
                    trans_dict[word]
                    if not re.match(r'-?\d+', word)
                    else int(word), numbers)
    except KeyError:
        raise ValueError(f'Unhandled word.')

    if type(sum_ := next(iter_, None)) is str: raise ValueError('Operand should be a number')
    while op := next(iter_, None):
        if type(op) is int: raise ValueError('Operator should be a string')
        if type(num_ := next(iter_, None)) is str: raise ValueError('Operand should be a number')
        sum_ = eval(f'{sum_}{op}{num_}')

    return sum_

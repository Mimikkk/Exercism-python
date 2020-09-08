from typing import *


class StackUnderflowError(Exception): pass


symbol_table = {}


def parse_definition(expression: List[str]):
    if (comps := expression.split())[1].isdigit(): raise ValueError(" Can not redefine number")
    symbol_table[comps[1]] = ' '.join(symbol_table[x] if x in symbol_table else x for x in comps[2:-1])

def is_register_definition(expression: List[str]) -> bool:
    return expression[0] == ':' and expression[-1] == ';'


def process(expression: List[str]) -> List[int]:

    def pop(count: int) -> Tuple[int, int]:
        if len(result) < count: raise StackUnderflowError("Error")
        return int(result.pop()), int(result.pop()) if count == 2 else None

    result: List[int] = []
    for r in [x for c in expression.split() for x in (symbol_table[c].split() if c in symbol_table.keys() else [c])]:
        if r.isdigit():
            result.append(int(r))
        elif r.lower() == 'drop':
            pop(1)
        elif r.lower() == 'dup':
            (x, _) = pop(1)
            result.append(x)
            result.append(x)
        elif r.lower() == 'swap':
            result.extend(pop(2))
        elif r.lower() == 'over':
            (x, y) = pop(2)
            result.append(y)
            result.append(x)
            result.append(y)
        elif r == '/':
            (x, y) = pop(2)
            if x == '0':
                raise ValueError("Division by 0")
            result.append(y // x)
        elif r == '*':
            (x, y) = pop(2)
            result.append(x * y)
        elif r == '+':
            (x, y) = pop(2)
            result.append(x + y)
        elif r == '-':
            (x, y) = pop(2)
            result.append(y - x)
        else:
            raise ValueError('Unrecognized symbol')
    return result


def evaluate(data: List[str]) -> List[int]:
    symbol_table.clear()
    for expression in map(lambda x: x.lower().strip(), data):
        if not is_register_definition(expression):
            return process(expression)
        parse_definition(expression)

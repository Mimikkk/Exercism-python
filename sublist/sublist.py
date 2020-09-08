
EQUAL = 0
SUBLIST = 1
SUPERLIST = 2
UNEQUAL = 3


def sublist(*args):
    str_1, str_2 = map(str, args)
    if str_1 == str_2:
        return EQUAL
    elif str_2[1:-1] in str_1:
        return SUPERLIST
    elif str_1[1:-1] in str_2:
        return SUBLIST
    return UNEQUAL

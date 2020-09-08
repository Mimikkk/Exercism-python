ROMAN = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def roman(n: int) -> str:
    result: str = ''

    for key in ROMAN:
        while n >= key:
            result += ROMAN[key]
            n -= key
    return result

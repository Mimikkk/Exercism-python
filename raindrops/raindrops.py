def convert(num: int) -> str:
    result: str = ""
    if num%3==0: result += "Pling"
    if num%5==0: result += "Plang"
    if num%7==0: result += "Plong"
    return result if result else str(num)

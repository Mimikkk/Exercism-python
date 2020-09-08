def is_isogram(string: str) -> bool:
    previous: set = set()

    e: chr
    for e in string.lower():
        if e.isalpha() and e in previous:
            return False
        else:
            previous.add(e)
    return True
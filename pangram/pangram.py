def is_pangram(sentence: str) -> bool:
    bool_: list = [False]*26
    for e in set(sentence.lower()):
        if e.isalpha():
            bool_[ord(e)-ord('a')] = True
    return all(bool_)

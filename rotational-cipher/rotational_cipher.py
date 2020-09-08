def rotate(text: str, key: int) -> str:
    return ''.join(chr(((ord(chr_) + key - key2) % 26) + key2) if chr_.isalpha() else chr_
                   for chr_ in text for key2 in [65 if chr_.isupper() else 97])

import string

atbash = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1], string.punctuation + ' ')


def encode(str_: str) -> str:
    encoded = str_.lower().translate(atbash)
    return ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))


def decode(str_: str) -> str:
    return str_.translate(atbash)

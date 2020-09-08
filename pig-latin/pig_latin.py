import re


def translate(text: str) -> str:
    return " ".join(map(encode, text.split()))

def encode(word: str) -> str:
    return word[len(prefix := re.search("(y|.*?(qu)?)([aeiouy]|xr|yt)", word).group(1)):] + prefix + "ay"

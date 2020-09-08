import re
def abbreviate(sentence: str) -> str:
    return ''.join(re.findall(r'([A-Z])[A-Z\']*', sentence.upper()))

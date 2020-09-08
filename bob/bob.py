import re
def response(sentence: str) -> str:
    sentence = sentence.strip()
    if not sentence: return "Fine. Be that way!"
    is_forceful: bool = sentence == sentence.upper() and bool(re.search(r'[A-Z]', sentence, flags=re.I))
    is_question: bool = sentence[-1] == "?"

    if is_forceful and is_question: return "Calm down, I know what I'm doing!"
    if is_question: return "Sure."
    if is_forceful: return "Whoa, chill out!"
    return "Whatever."

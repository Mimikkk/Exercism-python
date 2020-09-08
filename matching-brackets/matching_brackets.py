import re
def is_paired(str_: str) -> bool:
    str_ = re.sub(r'[^{}\[\]()]', '', str_)
    while str_ != (str_ := re.sub(r'{\}|\[]|\(\)', '', str_)): pass
    return not bool(str_)

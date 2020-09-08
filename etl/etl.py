from typing import *

def transform(legacy_data: Dict[int, List[chr]]) -> Dict[chr, int]:
    return {key.lower(): val for val, keys in legacy_data.items() for key in keys}

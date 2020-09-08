from typing import *
def slices(series: str, len_: int) -> List[str]:
    if len_ <= 0 or len(series) < len_: raise ValueError('Rawr xD')
    return [series[i:i+len_] for i in range(len(series)-len_+1)]

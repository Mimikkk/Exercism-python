from typing import *

command_dict: Dict[int, str] = {1: 'wink',
                                2: 'double blink',
                                4: 'close your eyes',
                                8: 'jump'}
REVERSE: int = 16

def commands(n: int) -> List[str]:
    result: List[str] = [command for (key, command) in command_dict.items() if n & key == key]
    return result[::-1] if n & REVERSE == REVERSE else result

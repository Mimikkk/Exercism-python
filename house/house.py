from typing import *


VERSES: Tuple[str, ...] = (
    'the house that Jack built',
    'the malt',
    'the rat',
    'the cat',
    'the dog',
    'the cow with the crumpled horn',
    'the maiden all forlorn',
    'the man all tattered and torn',
    'the priest all shaven and shorn',
    'the rooster that crowed in the morn',
    'the farmer sowing his corn',
    'the horse and the hound and the horn',
)

ACTIONS: Tuple[str, ...] = (
    'lay in',
    'ate',
    'killed',
    'worried',
    'tossed',
    'milked',
    'kissed',
    'married',
    'woke',
    'kept',
    'belonged to',
)

def recite(start: int, end: int) -> List[str]:
    return [f"{f'This is {VERSES[n]}'}{''.join(f' that {ACTIONS[i]} {VERSES[i]}' for i in reversed(range(n)))}."
            for n in range(start-1, end)]

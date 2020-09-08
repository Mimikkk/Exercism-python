from typing import *


def recite(start: int, take: int = 1) -> List[str]:
    bottles = start
    result: List[str] = []
    for i in range(take):
        beer_verse = lambda x: f"{x if x != 0 else 'No more'} bottle{'s' if x != 1 else ''} of beer"

        take_string = f"Take {'one' if bottles > 1 else 'it'} down and pass it around"
        store_string = f"Go to the store and buy some more"
        new_bottles = bottles - 1 if bottles > 0 else 99

        result.append(f"{beer_verse(bottles)} on the wall, {beer_verse(bottles).lower()}.")
        result.append(f"{take_string if bottles != 0 else store_string}, {beer_f(new_bottles).lower()} on the wall.")
        result.append("")

        bottles = new_bottles
    result.pop()
    return result

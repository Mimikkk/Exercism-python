from secrets import choice
from typing import *

def modifier(n: int) -> int: return (n - 10) // 2

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        range_: Sequence[int] = range(1, 7)
        return sum(sorted(choice(range_) for _ in range(6))[:3])


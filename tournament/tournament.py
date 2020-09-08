from typing import *

class Team(object):
    def __init__(self, name: str):
        self.name: str = name
        self.MP: int = 0
        self.W: int = 0
        self.D: int = 0
        self.L: int = 0
        self.P: int = 0

    def __str__(self):
        return f"{self.name:<30} |  {self.MP} |  {self.W} |  {self.D} |  {self.L} |  {self.P}"

    def __repr__(self):
        return f'Team({self.__str__()})'

    def __lt__(self, other: 'Team') -> bool:
        return self.name < other.name if self.P == other.P else self.P > other.P

    def played_against(self, other: 'Team', result: str):
        is_win: bool = result == 'win'
        is_draw: bool = result == 'draw'

        self.MP += 1
        other.MP += 1

        if is_draw:
            self.D += is_draw
            other.D += is_draw
        else:
            self.W += not is_win
            other.W += is_win
            self.L += is_win
            other.L += not is_win

        self.P += (1 if is_draw else (3 if not is_win else 0))
        other.P += (1 if is_draw else (3 if is_win else 0))

def create_header() -> str:
    return f'{"Team":<30} | MP |  W |  D |  L |  P'


def tally(data: List[str]) -> List[str]:

    teams: Dict[str, Team] = {}
    for (p1, p2, r) in map(lambda str_: str_.split(';'), data):
        if p1 not in teams: teams[p1] = Team(p1)
        if p2 not in teams: teams[p2] = Team(p2)
        teams[p2].played_against(teams[p1], r)

    return [create_header(), *map(str, sorted(teams.values()))]

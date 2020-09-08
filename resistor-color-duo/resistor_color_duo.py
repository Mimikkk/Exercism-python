from typing import *
COLORS = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
          'yellow': 4, 'green': 5,
          'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

color_code: Callable[[str], str] = lambda color: str(COLORS[color])
value: Callable[[List[str]], int] = lambda list_: int(''.join(map(color_code, list_[:2])))

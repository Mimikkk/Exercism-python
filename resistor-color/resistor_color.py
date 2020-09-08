from typing import *
COLORS = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
          'yellow': 4, 'green': 5,
          'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

color_code: Callable[[str], int] = lambda color: COLORS[color]
colors: Callable[[], List[str]] = lambda: list(COLORS.keys())

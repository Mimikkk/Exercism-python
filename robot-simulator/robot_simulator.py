from typing import *


class Point(object):
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)


class Direction(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.left: Optional['Direction'] = None
        self.right: Optional['Direction'] = None

    def connect(self, left: 'Direction', right: 'Direction'):
        self.left = left
        self.right = right


NORTH = Direction(0, 1)
SOUTH = Direction(0, -1)
EAST = Direction(1, 0)
WEST = Direction(-1, 0)
NORTH.connect(WEST, EAST)
EAST.connect(NORTH, SOUTH)
WEST.connect(SOUTH, NORTH)
SOUTH.connect(EAST, WEST)


class Robot(object):
    def __init__(self, direction: Direction = NORTH, x: int = 0, y: int = 0):
        self.direction: Direction = direction
        self.pos: Point = Point(x, y)

    def move(self, ops: str):
        for op in ops:
            if op == 'A':
                self.pos += self.direction
            else:
                self.direction = self.direction.left if op == 'L' else self.direction.right

    @property
    def coordinates(self):
        return self.pos.x, self.pos.y

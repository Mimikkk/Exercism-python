from string import ascii_uppercase as ALPHA, digits as DIGITS
from random import seed, choice

robot_names: list = []
class Robot(object):
    def __init__(self):
        self.name: str = ""
        self.reset()

    def __new_name(self):
        seed(None)
        self.name = ''.join(choice(x) for count, x in zip((2, 3), (ALPHA, DIGITS)) for _ in range(count))

    def reset(self):
        while not self.name or self.name in robot_names:
            if prev_name := self.name: robot_names.remove(prev_name)
            self.__new_name()
        robot_names.append(self.name)

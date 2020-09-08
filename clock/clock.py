class Clock(object):
    def __init__(self, hour: int, minute: int):
        self.hour = (hour + minute//60) % 24
        self.minute = minute % 60

    def __repr__(self) -> str:
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other: 'Clock') -> bool:
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, other) -> 'Clock':
        if type(other) is int:
            return Clock(self.hour, self.minute + other)
        raise ValueError(f'Unhandled Type {type(self)}+{type(other)}')

    def __sub__(self, other) -> 'Clock':
        if type(other) is int:
            return Clock(self.hour, self.minute - other)
        raise ValueError(f'Unhandled Type {type(self)}-{type(other)}')

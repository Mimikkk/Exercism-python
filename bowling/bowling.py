class BowlingGame:
    def __init__(self):
        self._pins = []
        self._frame = []

    def roll(self, pin):

        if len(self._pins) == 11 and sum(self._pins[-1]) != 10:
            raise ValueError('Cannot roll after bonus rolls for strike')
        if pin > 10 or pin < 0:
            raise ValueError(f'A roll cannot have {pin} points')

        if len(self._pins) > 9:
            if sum(self._pins[9]) != 10:
                raise ValueError('Cannot roll bonus if not strike nor spare')
            elif self._frame and self._pins[9] != [10]:
                raise ValueError('Cannot roll bonus roll after bonus for strike or spare')

        if pin == 10: self._pins.append([10])

        if self._frame:
            if pin + self._frame[0] > 10 and self._frame[0] != 10:
                raise ValueError('Two rolls in a frame cannot score more than 10 points')
            self._frame.append(pin)
            self._pins.append(self._frame)
            self._frame = []
        else:
            if pin != 10:
                self._frame.append(pin)

    def score(self):
        _score = []
        if self._frame: self._pins.append(self._frame)

        for (i, frame) in enumerate(self._pins):
            if sum(frame) < 10: _score.append(sum(frame))
            elif sum(frame) == 10:
                if i == 9:
                    _score.append(sum([roll for f in self._pins[9:] for roll in f]))
                    break
                _score.append(10 + (self._pins[i+1][0]
                                    if len(frame) > 1
                                    else sum((self._pins[i+1] + self._pins[i+2])[:2])))
            else: raise ValueError('A frame cannot score more than 10 points')
        return sum(_score)

STATUS_WIN = "won"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman(object):
    def __init__(self, word: str):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = list(word)
        self.masked = list("_" * len(word))

    def guess(self, chr_: chr):
        if self.status != STATUS_ONGOING: raise ValueError(f"You {self.status}!")

        if chr_ not in self.word or chr_ in self.masked:
            self.remaining_guesses -= 1
        else:
            for i, c in enumerate(self.word):
                if c == chr_:
                    self.masked[i] = c
        self._update_status()

    def get_masked_word(self):
        return ''.join(self.masked)

    def get_status(self):
        return self.status

    def _update_status(self):
        if self.remaining_guesses < 0: self.status = STATUS_LOSE
        elif self.masked == self.word: self.status = STATUS_WIN

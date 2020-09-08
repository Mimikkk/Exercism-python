# Score categories.
# Change the values as you see fit.

ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6

LITTLE_STRAIGHT = 7
BIG_STRAIGHT = 8

FULL_HOUSE = 9

CHOICE = 10
FOUR_OF_A_KIND = 11
YACHT = 12


def score(dice: list, category: int) -> int:
    dice.sort()
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return category * dice.count(category)

    if category == CHOICE:
        return sum(dice)

    if category == FULL_HOUSE:
        counts: list = [dice.count(e) for e in range(1, 7)]
        return sum(dice) if any(e == 3 for e in counts) and any(e == 2 for e in counts) else 0

    if category == LITTLE_STRAIGHT:
        return 30 if dice == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        return 30 if dice == [2, 3, 4, 5, 6] else 0

    if category == YACHT:
        return 50 if dice[0] == dice[-1] else 0

    if category == FOUR_OF_A_KIND:
        return 4*dice[2] if dice.count(dice[2]) >= 4 else 0

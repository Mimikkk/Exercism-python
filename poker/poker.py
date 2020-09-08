from functools import reduce
from typing import *
import re

STRAIGHT_FLUSH: int = 0
FOUR_OF_A_KIND: int = 1
FULL_HOUSE: int = 2
FLUSH: int = 3
STRAIGHT: int = 4
THREE_OF_A_KIND: int = 5
TWO_PAIR: int = 6
ONE_PAIR: int = 7
HIGH_CARD: int = 8
RANKING: Dict[str, int] = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, '10': 4, '9': 5, '8': 6,
                           '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}


def rank_hand(cards: Tuple[int, ...], colors: Tuple[str, ...]) -> Tuple[int, Tuple[int, ...]]:
    if cards == (0, 9, 10, 11, 12): cards = (9, 10, 11, 12, 13)

    is_straight: bool = all(cards[i - 1] == cards[i] - 1 for i in range(1, len(cards)))
    is_color: bool = all(colors[i - 1] == colors[i] for i in range(1, len(colors)))

    card_counts: Dict[int, int] = {card: cards.count(card) for card in sorted(set(cards))}
    pairs: Tuple[int, ...] = tuple(filter(lambda x: card_counts[x] == 2, card_counts))
    triple: Tuple[int, ...] = tuple(filter(lambda x: card_counts[x] == 3, card_counts))
    quadruple: Tuple[int, ...] = tuple(filter(lambda x: card_counts[x] == 4, card_counts))

    if is_straight and is_color: return STRAIGHT_FLUSH, tuple(cards)
    if quadruple: return FOUR_OF_A_KIND, quadruple + tuple(c for c in cards if c not in quadruple)
    if triple and pairs: return FULL_HOUSE, tuple([triple[-1], pairs[-1]])
    if is_straight: return STRAIGHT, tuple(cards)
    if is_color: return FLUSH, tuple(cards)
    if triple: return THREE_OF_A_KIND, triple + tuple(c for c in cards if c not in triple)
    if len(pairs) == 2: return TWO_PAIR, pairs + tuple(c for c in cards if c not in pairs)
    if pairs: return ONE_PAIR, pairs + tuple(c for c in cards if c not in pairs)
    return HIGH_CARD, tuple(cards)


def best_hands(hands: List[str]) -> List[str]:
    return [hand for scores
            in [tuple(map(lambda x: rank_hand(*x),
                          [(tuple(sorted(map(lambda card: RANKING[card], cards[::-1]))), colors)
                           for hand in hands
                           for (cards, colors) in [(zip(*re.findall(r'(\w*)(\w) ?', hand)))]]))]
            for high_score in [min(scores)]
            for (hand, score) in zip(hands, scores) if score == high_score]

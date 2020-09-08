from collections import Counter
from typing import *

prices_with_discounts = (0, 800, 1520, 2160, 2560, 3000)

def total(basket: List[int]) -> int:
    counted_books: Dict[int, int] = Counter(basket)
    price: int = 0
    book_number: List[int] = []

    while len(counted_books):
        price += prices_with_discounts[len(counted_books)]
        book_number.append(len(counted_books))

        counted_books = {k: v-1 for k, v in counted_books.items()}
        counted_books = {k: v for k, v in counted_books.items() if v != 0}

    while 3 in book_number and 5 in book_number:
        price -= 40
        book_number.remove(3)
        book_number.remove(5)

    return price

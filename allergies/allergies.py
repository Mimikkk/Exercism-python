from typing import *

class Allergies:
    allergens: Dict[int, str] = {1: "eggs",
                                 2: "peanuts",
                                 4: "shellfish",
                                 8: "strawberries",
                                 16: 'tomatoes',
                                 32: 'chocolate',
                                 64: 'pollen',
                                 128: "cats"}

    def __init__(self, score):
        self.allergy_list: List[str] = [allergen for (key, allergen) in self.allergens.items() if score & key == key]

    def allergic_to(self, item):
        return item in self.allergy_list

    @property
    def lst(self):
        return self.allergy_list

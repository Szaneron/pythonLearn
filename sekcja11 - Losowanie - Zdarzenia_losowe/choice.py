"""
choice - zwraca losowy element
choices - zwraca listę elementów i ma większe możliwości

"""

import random

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia", "losowa rzecz"]

nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]

from collections import Counter

print(Counter(random.choices(nagrodaZeSkrzynki, [0.8, 0.15, 0.04, 0.01], k = 100)))

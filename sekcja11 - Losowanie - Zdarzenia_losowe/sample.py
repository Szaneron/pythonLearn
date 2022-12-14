"""
Napisz funkcję, która zasymuluje jak działa lotto,
tzn. wybiersz 6 UNIKALNYCH liczb z 49

sample - próbka/przykład

"""

import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace"
            "Joker", "Joker"]

random.shuffle(cardList)
player1_list = []
player2_list = []

print("Talia kart: ", cardList)

for card in range(5):
    player1_list.append(cardList.pop())

for card in range(5):
    player2_list.append(cardList.pop())


print("Karty gracza 1: ", player1_list)
print("Karty gracza 2: ", player2_list)
print("Pozostała talia kart: ", cardList)

"""[0,1,2....49]"""
def choose_random_numbers(amount, total_amount):    
    print(random.sample(range(total_amount + 1), amount))


def random_numbers(amount, total_amount):
    numbers = []
    while len(numbers) < amount:
        random_number = random.randint(0, total_amount)
        if random_number not in numbers:
            numbers.append(random_number)
        else:
            continue
    print(numbers)


random_numbers(6, 10)
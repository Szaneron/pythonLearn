"""
random - z ang. losowy

random()            0 <= x < 1 lub [0,1)

uniform(2.5, 10.0)  2.5 <= x < 10.0 lub [2.5, 10)

randrange(10)       z puli (0,1,2,3,4,5,6,7,8,9)
randrange(0, 15, 2) parzyste z puli (0,2,4..14)

randint(0, 4) [0,4]
"""

import random


def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0,100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"


x = 0

listHit = []

while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))

from collections import Counter

dictionaryHit = Counter(listHit)

x = 0
while x < 100:
    x = x + 1
    print(random.randint(0,10))

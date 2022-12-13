"""
Zsumuj wszystkie liczby od 0 do 100 podniesione do potęgi 2
"""

numberGenerator = (number ** 2
                   for number in range(100)
                   )

# print(numberGenerator)
# for item in numberGenerator:
#     print(item)

print(sum(numberGenerator))
"""
Znajdź liczby od 2 do 470 włącznie, które są:
- podzielne przez 7, ale nie są podzielne przez 5

Z czego skorzystasz?
1) generatora
2) wyrażenia listowego
3) wyrażenia zbioru
4) wyrażenia słownikowego

Zastanów się, czy odpowiedź na to pytanie jest zawsze taka sama?
"""
# numbers = []
# for number in range(2,471):
#     numbers.append(number)
#
# print(numbers)

method1 = (number
           for number in range(2,471)
           if (number % 7 == 0)
           if (number % 5 != 0)
)
for item in method1:
    print(item)

method2 = [number
           for number in range(2,471)
           if (number % 7 == 0)
           if (number % 5 != 0)
]
print(method2)

method3 = {
        number
        for number in range(2,471)
        if (number % 7 == 0)
        if (number % 5 != 0)
}
print(method3)

method4 = {
    number : number
    for number in range(2, 471)
    if (number % 7 == 0)
    if (number % 5 != 0)
}
print(method4)
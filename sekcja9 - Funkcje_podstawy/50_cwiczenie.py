'''
Napisz funkcję, która jako argument przyjmuje listę liczb i zwraca
sumę wszystkich liczb dodatnich na liście.
Funkcja powinna ignorować wszelkie liczby ujemne lub zera na liście.
'''

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# pętla:
def sum_positives1(numbers):
    sum = 0

    for number in numbers:
        if number % 2 == 0 and number > 0:
            sum += number

    return sum

print(sum_positives1(numbers))


# lista wyrażeniowa:
def sum_positives2(numbers):
    return sum([number
                for number in numbers
                if number % 2 == 0
                if number > 0
                ])

print(sum_positives2(numbers))
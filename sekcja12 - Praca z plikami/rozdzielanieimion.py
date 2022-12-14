"""
ĆWICZENIE:

Wczytaj imiona i nazwiska z pliku o nazwie:
imionanazwiska.txt

1) rozdziel je tak, by powstała lista krotek, gdzie wewnętrzne krotki to
pary imiona/nazwiska
2) zapisz imiona do pliku imiona.txt
3) zapisz nazwiska do pliu nazwiska.txt

Zastanów się jak rozwiązać problem,
gdy nie ma podanego nazwiska w pliku imionanazwiska.txt, gdy będziesz
zapsywał nazwiska do pliku nazwiska.txt


[
 ("Arkadiusz", "Włodarczyk"),
 ("Jakis", "Ziom")
]

"""

namesandsurnames = []

with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesandsurnames.append(tuple(line.replace("\n", "").split(" ")))

print(namesandsurnames)

with open("imiona.txt", "w", encoding="UTF-8") as file:
    for name in namesandsurnames:
        file.write(name[0] + "\n")

with open("nazwiska.txt", "w", encoding="UTF-8") as file:
    for surname in namesandsurnames:
        try:
            file.write(surname[1] + "\n")
        except:
            file.write("\n")
dictionary = {}

while(True):
    print("1: Dodaj nową definicję.")
    print("2: Znajdź definicję.")
    print("3: Usuń definicję.")
    print("4: Zamknij program.")
    print()
    choice = input("Co chcesz zrobić?")

    if (choice == "1"):
        key = input("Podaj słowo które ma być dodane do słownika: ")
        definition = input("Podaj definicję tego słowa: ")
        dictionary[key] = definition
        print("Definicja zsotała dodana do słownika.")

    elif (choice == "2"):
        key = input("Do jakiego słowa szukasz definicji?")
        if key in dictionary:
            print(dictionary[key])
        else:
            print("Nie znaleziono definicji dla słowa:", key)

    elif (choice == "3"):
        key = input("Jakie słowo chcesz usunąć ze słownika?")
        if key in dictionary:
            del dictionary[key]
            print("Słowo zostało usunięte ze słownika.")
        else:
            print("Nie znaleziono danego słowa:", key)

    elif (choice == "4"):
        print("Zamykanie programu")
        break

    else:
        print("Nieobsługiwane polecenie.")
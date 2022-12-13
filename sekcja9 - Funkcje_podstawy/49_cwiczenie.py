'''
ĆWICZENIE: Program liczący powierzchnie figur
Stwórz menu, z którego użytkownik, może wybrać opcje, aby policzyć powierzchnie figur:

1) prostokąta
2) kwadratu
3) trójkąta
4) trapezu
5) koła

Pamiętaj, by skorzystać z funkcji.
'''
import math

def prostokat(a, b):
    return a * b

def kwadrat(a):
    return a * a

def trojkat(a, h):
    return (a * h) / 2

def trapez(a, b, h):
    return ((a + b) * h) / 2

def koło(r):
    return math.pi * (r**2)

while True:
    print("1: Prostokąt")
    print("2: Kwadrat")
    print("3: Trójkąt")
    print("4: Trapez")
    print("5: Koło")
    print("6: Zamknij program")
    choice = input("Wybierz akcję: ")

    if (choice == "1"):
        a = int(input("Podaj długość boku a: "))
        b = int(input("Podaj długość boku b: "))
        print("Pole figury: ", prostokat(a, b))
        print()

    if (choice == "2"):
        a = int(input("Podaj długość boku a: "))
        print("Pole figury: ", kwadrat(a))
        print()

    if (choice == "3"):
        a = int(input("Podaj długość boku a: "))
        h = int(input("Podaj wysokść h: "))
        print("Pole figury: ", trojkat(a, h))
        print()

    if (choice == "4"):
        a = int(input("Podaj długość boku a: "))
        b = int(input("Podaj długość boku b: "))
        h = int(input("Podaj wysokść h: "))
        print("Pole figury: ", trapez(a, b, h))
        print()

    if (choice == "5"):
        r = int(input("Podaj długość promienia r: "))
        print("Pole figury: ", koło(r))
        print()

    elif (choice == "6"):
        print("Zamykanie programu")
        break



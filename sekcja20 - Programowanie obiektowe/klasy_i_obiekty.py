"""

OOP - Object Oriented Programming

Programowanie zorientowane wokół obiektów

OBIEKT

OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznie ze
          sobą powiązanych do dalszego łatwiejszego ponownego użycia

Klasy   - foremki (szablony) do tworzenia egzemplarzy obiektów

Atrybut - cecha opisująca obiekt
Metoda - funkcja, która operuje na obiekcie


Instacja klasy - instance z ang. egzemplarz to obiekt, który wyszedł z formy (klasy)


"""


class User:
    age = 0


seba = User()
mirek = User()
arek = User()

mirek.age = 24

age = 40

print(seba.age)
print(mirek.age)
print(arek.age)
print(age)


class Monitor:
    height = 0
    weight = 0


monitor1 = Monitor()
monitor2 = Monitor()

monitor1.height = 1024
monitor1.weight = 2048

monitor2.height = 1024
monitor2.weight = 1024

print(monitor1.weight)
print(monitor2.weight)

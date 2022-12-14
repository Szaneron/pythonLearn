'''
Stwórz funkcję, która obsługuje otwieranie pliku do wczytywania danych.

Zapytaj się użytkownika o nazwę pliku, który chce otworzyć do wczytania.

Jeśli plik nie istnieje wypisz mu odpowiedni komunikat.

Jeśli plik istnieje wczytaj całą jego zawartość i zwróć jako wynik funkcji.
'''


def readFile(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Nie ma takiego pliku")

fileName = input("Nazwa pliku: ")

fileContent = readFile(fileName)
print(fileContent)
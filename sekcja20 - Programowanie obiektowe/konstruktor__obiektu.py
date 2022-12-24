"""
__init__ - initialization - inicjalizacja - czyli ustawienie startowych 
           wartości dla atrybutów

w innych językach __init__ to konstruktor

"""


class User:  # z dużej litery klasy

    def __init__(self, age, name):
        print(
            "jestem inicjalizatorem, ktory wywoluje sie zawsze podczas konstrukcji obiektu")

        self.age = age
        self.name = name

        self.ageInFuture = age + 1

    def print_age(self, message):
        print(message, "wiek: ", self.age, self.name)


user1 = User(30, "Arek")
user2 = User(24, "Mirek")

user1.print_age("dodatkowy tekst całkowicie inny")
user2.print_age("dodatkowy tekst")

print(user1.ageInFuture)

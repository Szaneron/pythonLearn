"""
OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznie ze
          sobą powiązanych do dalszego łatwiejszego ponownego użycia

Klasy   - foremki (szablony) do tworzenia egzemplarzy obiektów

Atrybut - cecha opisująca obiekt
Metoda - funkcja, która operuje na obiekcie

self - z ang. 'ja', 'sam osobiście', 'siebie' w innych językach: 'this'

"""

age = 450


class User:  # z dużej litery klasy
    age = 0
    name = ""

    def print_age(self, message):
        print(message, "wiek: ", self.age, self.name)

    def another_method(self):
        pass

    def another_method2(self, message, blablaa):
        pass


user1 = User()
user2 = User()

userList = [User(), User()]

userList[0].age = 20
userList[1].age = 30

userList[0].name = "Franiu"
userList[1].name = "Wiolka"

userList[0].print_age("")

user1.age = 30
user1.name = "Arek"
user1.print_age("dodatkowy tekst całkowicie inny")

user2.age = 24
user2.name = "Mirek"
user2.print_age("dodatkowy tekst")


def print_age(name, age):
    print(name, "wiek: ", age)


name = "Arek"
print_age(name, age)

'''

Otrzymujesz listę osób, które dostaną 'dostęp' do tajnych informacji:
imiona = ['Arkadiusz', 'Wiola', 'Antek']

Jeśli ktoś z listy 'imiona' zostanie podany przez użytkownika w zmiennej 'imie'
wyświetl:
"Masz dostęp"

Jeśli nie wypisz:
"Brak dostępu"

'''

imiona = ['Arkadiusz', 'Wiola', 'Antek']
imie = input("Podaj imie: ")
imie = imie.capitalize()

if imie in imiona:
    print("Masz dostęp")
else:
    print("Brak dostępu")
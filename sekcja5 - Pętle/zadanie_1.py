i = 0
result = 0

while i < 3:
    x = int(input("Podaj liczbę parzystą dodatnią:"))
    if x > 0 and x % 2 == 0:
        result += x
    elif x < 0 and x % 2 == 0:
        print("Liczba nie jest dodatnia")
        continue
    elif x > 0 and x % 2 != 0:
        print("Liczba nie jest parzysta")
        continue
    i += 1

print("Wynik dodawania to: ", result)
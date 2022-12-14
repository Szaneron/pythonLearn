"""
    obiekt to zmienna, która ma więcej możliwości,
    można wywołać na nim "funkcje"
    może mieć więcej niż 1 wartość
    
    obiekty immutable: bool, int, float, tuple, str

    immutable - niezmmienne
    mutable - zmienny

    = ZMIANA miejsca wskazywania na nowy adres, na inny obiekt
"""



listSample = [1, 4, 512, 24]


k = 4
h = 4

c = 5
#print(id(c))
def add(c, amount = 1):
    print(id(c))
    c = c + amount
    print(id(c))

#add(c)

def append_element_to_list(listka, element):
    print(id(listka))
    a = [2, 4, 20] 
    listka = a 
    print(id(listka))



print(id(listSample))
append_element_to_list(listSample, 5)



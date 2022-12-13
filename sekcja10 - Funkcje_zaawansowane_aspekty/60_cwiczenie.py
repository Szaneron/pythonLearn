'''
Napisz funkcję która dla przykładu po wywołaniu:

print(count(2,4,1,2,4,5, 10))

pokaże jako wynik:

28

czyli sumę wszystkich argumentów.

'''

def count(*arg):
    sum = 0
    for element in arg:
        sum += element
    return sum

print(count(2,4,1,2,4,5, 10))
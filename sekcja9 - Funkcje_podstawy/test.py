#Użyj funkcji any(), aby określić, czy przeslana lista zawiera liczby parzyste


numbers1 = [1, 3, 5, 6, 7]
numbers2 = [1, 3, 5, 7, 9]
numbers3 = [2, 4, 6, 8]

def any_even(lista):
    return any([nr % 2 == 0 for nr in lista])

def all_even(lista):
    return all([nr % 2 == 0 for nr in lista])

print(any_even(numbers1))
print(any_even(numbers2))

if (any_even(numbers1)):
    print("tak jest tu parzysta")
else:
    print("nie")

if (any_even(numbers2)):
    print("tak jest tu parzysta")
else:
    print("nie")
    


# any - jakikolwiek - funkcja any SPRAWDZA, czy JAKAKOLWIEK wartość to True
# all - WSZYSTKIE

john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}

jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}

def has_required_skills(person, skills):
    return all(skill in person['skills'] for skill in skills)

required_skills = ['Python', 'JavaScript']

print(has_required_skills(john, required_skills))
print(has_required_skills(jane, required_skills))
"""
indent=4,
sort_keys=True

"""

import json

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

encodedFilm = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False, indent=4)


#print(encodedFilm)

with open("sample.json", encoding="UTF-8") as file:
    wynik = json.load(file)

#print(json.dumps(wynik, indent=4, ensure_ascii=False, sort_keys=True))

import pprint
print(wynik)
pprint.pprint(wynik)

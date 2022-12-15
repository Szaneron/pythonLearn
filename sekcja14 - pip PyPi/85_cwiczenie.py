'''
Wyobraź sobie, że szef zlecił Ci zadanie otwarcia z jego pliku tekstowego
1500 stron i przefiltrowania ichw taki sposób,
aby podać mu tylko te, które działają.
Szef chce, abyś działające strony zapisał do pliku tekstowego.

'''
import requests

allLinks = []
workingLinks = []
notWorkingLinks = []
restLinks = []

with open("links.txt", "r", encoding="UTF-8") as file:
    for line in file:
        allLinks.append((line.replace("\n", "")))

print(allLinks)

for line in allLinks:
    print(line)
    response = requests.get(line)
    print(response.status_code)
    if response.status_code == 200:
        workingLinks.append(line)
    elif response.status_code != 200:
        notWorkingLinks.append(line)

print(workingLinks)
print(notWorkingLinks)
print(restLinks)
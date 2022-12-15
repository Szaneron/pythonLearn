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
    try:
        response = requests.get(line)
        if response.status_code == 200 or 403:
            workingLinks.append(line)

    except requests.exceptions.ConnectionError:
        notWorkingLinks.append(line)

print(workingLinks)
print(notWorkingLinks)

with open("workingLinks.txt", "w", encoding="UTF-8") as file:
    for link in workingLinks:
        file.write(link + "\n")

with open("notWorkingLinks.txt", "w", encoding="UTF-8") as file:
    for link in notWorkingLinks:
        file.write(link + "\n")
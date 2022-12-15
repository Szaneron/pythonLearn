import requests
import json
import webbrowser
from pprint import pprint

params = {
    "amount": 5
}

r = requests.get('https://cat-fact.herokuapp.com/facts/random', params)

try:
   content = r.json()
except json.decoder.JSONDecodeError:
   print("Niepoprawny format")
else:
   for cat in content:
       print(cat["text"])



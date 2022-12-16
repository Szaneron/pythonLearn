import requests
import json
import webbrowser
import credentials

from pprint import pprint


r = requests.get('https://api.thecatapi.com/v1/favourites/',
                 headers=credentials.headers)


try:
   content = r.json()
except json.decoder.JSONDecodeError:
   print("Niepoprawny format", r.text)
else:
   print(content)


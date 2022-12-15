import requests
import json
"""

API - Application Programming Interface

Inter - pmiędzy
face - twarz

bankomat

"""



r = requests.get("")


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")

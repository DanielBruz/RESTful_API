"""
Zde je jednoduchý příklad komunikace s RESTful API pomocí Pythonu s využitím knihovny requests.
V tomto příkladu jsme vytvořili HTTP GET požadavek na zadanou adresu RESTful API a získali data ve formátu JSON.
"""

import requests

# Adresa RESTful API
api_url = 'https://api.example.com/data'

# Vytvoření HTTP GET požadavku
response = requests.get(api_url)

# Zpracování odpovědi
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Chyba při získávání dat:', response.status_code)


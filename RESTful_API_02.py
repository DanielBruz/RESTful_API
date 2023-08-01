"""
OpenWeatherMap API: Toto API poskytuje aktuální a předpovědi počasí pro různé lokace po celém světě.

(Nejprve je třeba se zaregistrovat na webových stránkách OpenWeatherMap (https://openweathermap.org/) a
získate klíč API, který budu potřebovat pro přístup k jejich API.)

V tomto příkladu jsme pomocí API získali aktuální počasí v Londýně a zobrazili jsme ho v konzoli.
"""

import requests
import json

api_key = '487549dc21a0c881cf5588100de765c3'

# Adresa API pro získání aktuálního počasí pro město: (defaultně mode = JSON)
api_url = f'http://api.openweathermap.org/data/2.5/weather?q=London&lang=cz&appid={api_key}'

# Vytvoření HTTP GET požadavku:
response = requests.get(api_url)

# Zpracování odpovědi:
if response.status_code == 200:
    data = response.json()

    with open("weather_data.json", "w") as fp:
        json.dump(data, fp)

    weather = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15  # Převod na stupně Celsius (dalo by se nahradit "&units=metric" v URL)
    print(f'Aktuální počasí v Londýně: {weather}')
    print(f'Teplota: {temperature:.2f} °C')
else:
    print('Chyba při získávání dat:', response.status_code)


"""
Převod JSON objektu/souboru na Python dictionary
"""

import json

print("Started Reading JSON file")
with open("weather_data.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    weather = json.load(read_file)

    print("Decoded JSON Data From File")
    for key, value in weather.items():
        print(key, ":", value)
    print("Done reading json file")

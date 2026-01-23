# Project #5 - Weather CLI App
# Get an user input : Name of city
# Output : Temperature, Feels_like, Humidity, Wind
# Handle errors
# Make output nicer
# minimal file structure : main, api files (seperately)
# do not leak API key : why?
# improve the program

import requests

API_KEY = "d350ff479977493d4d4624d2dff8ab03"
city = "Seoul"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",   # Celsius
    "lang": "kr"         # Korean descriptions (optional)
}

r = requests.get(url, params=params)
print(r.status_code)
print(r.text)  # raw JSON string



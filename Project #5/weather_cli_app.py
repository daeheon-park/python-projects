# Project #5 - Weather CLI App
# Get an user input : Name of city
# Output : Temperature, Feels_like, Humidity, Wind
# Handle errors
# Make output nicer
# minimal file structure : main, api files (seperately)
# do not leak API key : why?
# improve the program

import requests

API_KEY = "GO openWeather"
url = "https://api.openweathermap.org/data/2.5/weather"

#print(response.status_code)
#print(response.text)  # raw JSON string

def show_weather(city,data): # data.get{"main", {}} -> safer code. / dont ussume keys always exist
    # str -> None
    print(f"{city}'s weather information: ")
    print(f"""temperature : {data["main"]['temp']:.1f} 
    feels_like : {data["main"]["feels_like"]:.1f}
    humidity : {data["main"]["humidity"]:.1f}
    wind : {data["wind"]["speed"]:.1f}
""")

while True:
    city = input("Type city name: ").strip().lower()
    params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",   # Celsius
    "lang": "kr"         # Korean descriptions (optional)
    }

    try: 
        response = requests.get(url, params=params,timeout=10)
    except requests.exceptions.RequestException: 
        print("Network error.")
    else:
        if response.status_code == 200:
            data = response.json()
            show_weather(city,data)
        elif response.status_code == 404:
            print("City Not Found")
            continue
        elif response.status_code == 401:
            print("API Key Problem.")
        else:
            print("Other error.")

    exit_all = False

    while True:
        more_weather = input("Would you like to check another city? Y/N: ").strip().lower()
        if more_weather == 'y':
            break
        elif more_weather == 'n':
            exit_all = True
            break
        else:
            print("Please type Y/N.")
            continue
    
    if exit_all == True:
        break
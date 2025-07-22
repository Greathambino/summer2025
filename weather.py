'''
1: !!! First navigate to the correct directory !!!

2: python3 -m venv <name>

3: source <name>/bin/activate <-- for mac/linux
    <name>\Scripts\activate <-- for windows

4: python3 -m pip list <-- shows what is installed & what versions

pypi.org <-- search for packages online (documentation)
'''

import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()  # Load environment variables from .env file

def get_current_weather():
    print(f'\n*** Get Current Weather Conditions ***\n')

    city = input(f'\nPlease enter a city name:\n')

    requestURL = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    #print(requestURL) # Uncomment to see the request URL

    weather_data = requests.get(requestURL).json()
    #pprint(weather_data) # Uncomment to see the full weather data

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]} degrees Fahrenheit')
    print(f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]} degrees Fahrenheit.')
    

if __name__ == "__main__":
    get_current_weather()


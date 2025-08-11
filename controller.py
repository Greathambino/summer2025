import os, requests

def weather_data_controller(cityName):
    print(cityName)
    requestURL = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={cityName}&units=imperial'
    weather_data = requests.get(requestURL).json()

    if weather_data.get("cod") == '404':
        return {"success": False, "message": "City not found"}

    # output = f'\nCurrent weather for {weather_data["name"]}' + f'\nThe temp is {weather_data["main"]["temp"]} degrees Fahrenheit' + f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]} degrees Fahrenheit.'

    # it is optimal to just return the json data or just weather_data["temp"]

    with open('historyOfLocations.txt', 'a') as file:
        print(f'{weather_data}')
        file.write(f'{weather_data["name"]}, ')
        file.close()
    
    return weather_data

def history_controller():
    f = open('historyOfLocations.txt', 'r')
    history = f.read()
    f.close()
    return history
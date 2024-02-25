import requests

def weather_by_city(city):
    url = f'https://wttr.in/{city}'
    response = requests.get(url)
    return response.text

print(weather_by_city('Punta Cana'))
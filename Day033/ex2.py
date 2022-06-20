import requests
from datetime import datetime

MY_LAT = -23.454338
MY_LONG = -46.533669

params = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get(url=' https://api.sunrise-sunset.org/json', params=params)
response.raise_for_status()

print(response.json())

sunrise = int(response.json()['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(response.json()['results']['sunset'].split('T')[1].split(':')[0])

current_hour = datetime.now().hour

print(current_hour, sunrise, sunset)
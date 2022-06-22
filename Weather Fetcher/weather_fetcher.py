#IMPORT MODULES
import requests
import config

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#GETTING INPUT(CITY) FROM THE USER
city = input("Enter city: ")
request_url = f"{BASE_URL}?q={city}&appid={config.API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print("Weather: " + data["weather"][0]["description"])
    print("Temperature:", round(data["main"]["temp"] - 273.15, 2), "degrees celsius") #not sure about the conversion of farenheit to celsius
else:
    print("An error occurred.")
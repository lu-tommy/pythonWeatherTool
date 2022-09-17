import requests
from keys import *
apikey = apikey
city = str(input('enter city: '))
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={apikey}")
temp = str(round(response.json()['main']['temp']))
l_temp = str(round(response.json()['main']['temp_min']))
h_temp = str(round(response.json()['main']['temp_max']))
feel_like = str(round(response.json()['main']['feels_like']))
weather_desc = str(response.json()['weather'][0]['description'])

print(temp, '°f')
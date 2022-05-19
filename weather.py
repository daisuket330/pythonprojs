import requests

api_key = "9122543327dbd0a9cb68a52feda751ac"
city = "Tampa"
flat = 27.964157
flon = -82.452606
# url = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&{lon}&"&appid="+api_key

# https://api.openweathermap.org/data/2.5/weather?lat=27&lon=-82&appid=9122543327dbd0a9cb68a52feda751ac

url = "https://api.openweathermap.org/data/2.5/weather?lat=27&lon=-82&appid=9122543327dbd0a9cb68a52feda751ac&units=imperial"

request = requests.get(url)

json = request.json
json
print(json)
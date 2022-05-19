from urllib import request
import requests

api_key ="9122543327dbd0a9cb68a52feda751ac"
city = "Tampa"
url ="https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"

request = requests.get

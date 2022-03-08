import requests

URL = "https://api.battlemetrics.com/servers"

searchTerm = "Rustopia EU Main"

PARAMS = {"filter[search]":searchTerm,"filter[game]":"rust"}




x = requests.get(url = URL, params = PARAMS)

data = x.json()

print(data)

print(x)


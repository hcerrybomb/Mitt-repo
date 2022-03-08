import requests
import json
newURL = "https://api.battlemetrics.com/players/match?data[identifier]='76561198313072306'&data[type]='steamID'&data='identifier'&access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImQ2NzY0ZjU3OTcwY2ZlYmYiLCJpYXQiOjE2NDY1NjU2NTUsIm5iZiI6MTY0NjU2NTY1NSwiaXNzIjoiaHR0cHM6Ly93d3cuYmF0dGxlbWV0cmljcy5jb20iLCJzdWIiOiJ1cm46dXNlcjo1Mjk3NTMifQ.CCAsM9QodXjl1OUi-dqY-PFnv5_2_d6J8eShuNuJ9oQ"

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImQ2NzY0ZjU3OTcwY2ZlYmYiLCJpYXQiOjE2NDY1NjU2NTUsIm5iZiI6MTY0NjU2NTY1NSwiaXNzIjoiaHR0cHM6Ly93d3cuYmF0dGxlbWV0cmljcy5jb20iLCJzdWIiOiJ1cm46dXNlcjo1Mjk3NTMifQ.CCAsM9QodXjl1OUi-dqY-PFnv5_2_d6J8eShuNuJ9oQ'

URL = "https://api.battlemetrics.com/players/match"

identifier = '76561198313072306'

PARAMS = {
    'data[identifier]':identifier,
    'data[type]':'steamID',
    'data':'identifier'
}

DATA = {
  "data": [
    {
      "type": "identifier",
      "attributes": {
        "type": "steamID",
        "identifier": "76561198171172242"
      }
    }
  ]
}

#DATA = [{
#   'url':'/players/match',
#    'params':{
#        'data[identifier]':identifier,
#        'data[type]':'steamID',
#        'data':'identifier' 
#    },
#    'method':'post'
#}]



HEADERS = {
    'Content-Type':'application/json',
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImQ2NzY0ZjU3OTcwY2ZlYmYiLCJpYXQiOjE2NDY1NjU2NTUsIm5iZiI6MTY0NjU2NTY1NSwiaXNzIjoiaHR0cHM6Ly93d3cuYmF0dGxlbWV0cmljcy5jb20iLCJzdWIiOiJ1cm46dXNlcjo1Mjk3NTMifQ.CCAsM9QodXjl1OUi-dqY-PFnv5_2_d6J8eShuNuJ9oQ'
}

#x = requests.post(newURL)

x = requests.post(url=URL,data=json.dumps(DATA),headers=HEADERS)
print(x.url)
data = x.json()

parsed_data = json.dumps(data,indent=4,sort_keys=True)

print(parsed_data)
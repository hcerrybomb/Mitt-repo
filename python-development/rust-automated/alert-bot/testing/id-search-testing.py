import requests
import json 
from datetime import datetime
import difflib
import pprint
import os
import sys
import time



def send_to_json(file, json):
    with open(os.path.join(sys.path[0], file),"w") as outfile:
        outfile.write(json)



# Make formatted time string 1 month before now
now = datetime.now()
now = str(now)
now = list(now)
now[10] = "T"; now[19] = "Z"
now = now[0:20]
month = now[5] + now[6]
year = now[0]+now[1]+now[2]+now[3]
INTmonth = int(month) 
if INTmonth == 1:
    now[5] = "1"
    now[6] = "2"
    now[3] = int(now[3]) - 1
    now[3] = str(now[3])
else:
    if INTmonth >10:
        INTmonth -= 1
        now[5] = "1"
        now[6] = str(INTmonth - 10)
    else:
        now[5] = "0"
        now[6] = str(INTmonth - 1)
now = "".join(now)


PLAYER_URL = "https://api.battlemetrics.com/players"
PLAYER_SEARCH_TERM = "123" 
PLAYER_STEAM_ID = "76561198281556484"
#PLAYER_SERVER_SEARCH_TERM = "RJIAOSJDIASDJOPASMMINAIMSDMINO"
PLAYER_PARAMS = {
    "filter[search]":PLAYER_SEARCH_TERM,
    "filter[after]":now,
    "filter[server][game]":"rust",
    #"filter[server][search]":PLAYER_SERVER_SEARCH_TERM,

}

player_request = requests.get(url = PLAYER_URL, params = PLAYER_PARAMS)
player_json = player_request.json()
player_parsed = json.dumps(player_json,indent=4,sort_keys=True)
player_dict = json.loads(player_parsed)
send_to_json("player-info.json",player_parsed)
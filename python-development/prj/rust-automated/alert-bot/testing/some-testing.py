import requests
import json 
from datetime import datetime
import difflib
import pprint
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
print(now)




URL = "https://api.battlemetrics.com/servers"

URL2 = "https://api.battlemetrics.com/players"

searchTerm = "Rustopia EU Main"

playerSearchTerm = "[SB] ostritch"

PARAMS = {
    "filter[search]":searchTerm,
    "filter[game]":"rust",
    }

playerPARAMS = {
    "filter[search]":playerSearchTerm,
    "filter[after]":now
}

x = requests.get(url = URL, params = PARAMS)
y = requests.get(url = URL2, params = playerPARAMS)

data2 = y.json()

data = x.json()

parsed_data2 = json.dumps(data2,indent=4,sort_keys=True)
parsed_data = json.dumps(data,indent=4,sort_keys=True)

#print(parsed_data2)

parsed_data_dict = json.loads(parsed_data)
parsed_data_dict2 = json.loads(parsed_data2)

#print(len(parsed_data_dict["data"]))
if False:
    for i in range(len(parsed_data_dict["data"])):
        print(parsed_data_dict["data"][i]["attributes"]["ip"])
        print(parsed_data_dict["data"][i]["attributes"]["name"])
        print(parsed_data_dict["data"][i]["attributes"]["players"])
        print(parsed_data_dict["data"][i]["attributes"]["status"])
        print(parsed_data_dict["data"][i]["id"])



#with open("C:\\Users\\wista002\\Desktop\\Mitt-repo\\python-development\\rust-automated\\alert-bot\\testing\\request.json","w") as outfile:
with open("C:\\Users\\Gaming_Dator_VII\\Desktop\\Mitt-repo\\python-development\\rust-automated\\alert-bot\\testing\\request.json","w") as outfile:
    outfile.write(parsed_data2)

difflib_matches = []
top_ten_searches = []
for i in range(10):
    top_ten_searches.append(parsed_data_dict2["data"][i]["attributes"]["name"])
    difflib_matches += difflib.get_close_matches(playerSearchTerm,top_ten_searches[-1:],n=1)
    if len(difflib_matches) > 0:
        print(difflib_matches[0])
        print(f"\n\nSearch string: \t\t\t\t {playerSearchTerm}  \n\nBattleMetrics top results list:")
        pprint.pprint(top_ten_searches,indent=4)
        print("match found ^ ")
        print(f"\nBattlmetrics closest match:\t\t {top_ten_searches[0]}")
        print(f"Program closest match:\t\t\t {difflib_matches[0]}      found on run {1} on index {i}\n")
        player_match_name = parsed_data_dict2["data"][i]["attributes"]["name"]
        player_match_id = parsed_data_dict2["data"][i]["id"]

if len(difflib_matches)== 0:
    for i in range(9):
        
        if len(difflib_matches) > 0:
            break
        
        y = requests.get(url = parsed_data_dict2["links"]["next"])
        data2 = y.json()
        parsed_data2 = json.dumps(data2,indent=4,sort_keys=True)
        parsed_data_dict2 = json.loads(parsed_data2)
        for x in range(10):
            top_ten_searches.append(parsed_data_dict2["data"][x]["attributes"]["name"])
            
            difflib_matches += difflib.get_close_matches(playerSearchTerm,top_ten_searches[-1:],n=1)
            if len(difflib_matches) > 0: 



                print(f"\n\nSearch string: \t\t\t\t {playerSearchTerm}  \n\nBattleMetrics top results list:")
                pprint.pprint(top_ten_searches,indent=4)
                print("match found ^ ")
                print(f"\nBattlmetrics closest match:\t\t {top_ten_searches[0]}")
                print(f"Program closest match:\t\t\t {difflib_matches[0]}      found on run {i+2} on index {x}\n")



                player_match_name = parsed_data_dict2["data"][x]["attributes"]["name"]
                player_match_id = parsed_data_dict2["data"][x]["id"]
                break

        
        if len(difflib_matches) > 0:
            break

print(f"player match id: {player_match_id}\nplayer match name: {player_match_name}")


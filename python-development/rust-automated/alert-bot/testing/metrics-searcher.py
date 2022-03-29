import requests
import json 
from datetime import datetime
import difflib
import pprint
import os
import sys
import time

exit_loop = False
server_list = []
player_list = []
player_links_list = []
server_links_list =[]

# Sends response object to json file
def send_to_json(file, json):
    with open(os.path.join(sys.path[0], file),"w") as outfile:
        outfile.write(json)



# Make formatted time string 1 month before now
if True:

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

start = time.time()



# Creates a Dict of rust players with search term

if True:
    PLAYER_URL = "https://api.battlemetrics.com/players"
    PLAYER_SEARCH_TERM = ".crack TisU" 
    #PLAYER_SERVER_SEARCH_TERM = "RJIAOSJDIASDJOPASMMINAIMSDMINO"
    PLAYER_PARAMS = {
        "filter[search]":PLAYER_SEARCH_TERM,
        "filter[after]":now,
        "filter[server][game]":"rust",
        #"filter[server][search]":PLAYER_SERVER_SEARCH_TERM,
        #"filter[servers]":"ID GOES HERE",
    }

    player_request = requests.get(url = PLAYER_URL, params = PLAYER_PARAMS)
    player_json = player_request.json()
    player_parsed = json.dumps(player_json,indent=4,sort_keys=True)
    player_dict = json.loads(player_parsed)
    send_to_json("player-info.json",player_parsed)


    for i in range(10):
        for y in range(10):
            try:
                player_list.append(player_dict["data"][y]["attributes"]["name"])
                player_list.append(player_dict["data"][y]["id"])
            except IndexError:
                exit_loop = True
        
            
            
        try:
            next_link = player_dict["links"]["next"]
            player_links_list.append(next_link)
            player_request = requests.get(url = next_link)
            player_json = player_request.json()
            player_parsed = json.dumps(player_json,indent=4,sort_keys=True)
            player_dict = json.loads(player_parsed)
            send_to_json("player-info.json",player_parsed)
        except KeyError:
            break
        if exit_loop:
            break
        

    pprint.pprint(player_list,indent=4)

    print(len(player_list))

    pprint.pprint(player_links_list,indent=4)

    player_matches_list = difflib.get_close_matches(PLAYER_SEARCH_TERM,player_list,n=20,cutoff=0.4)

    pprint.pprint(player_matches_list)

    if len(player_matches_list) > 1:
        print(player_matches_list[0:2])
        print(set(player_matches_list[0:2]))
        if len(set(player_matches_list[0:2])) == 1:
            
            dupe_count = 2
            max_dupe_count = 5
            max_count = False
            for i in range(dupe_count,max_dupe_count):
                if len(set(player_matches_list[0:dupe_count])) == 1:
                    dupe_count+=1
                if dupe_count == 5:
                    print(f"max amt of dupes ({dupe_count}) found")
                    print("duplicates found, not accurate enough, consider adding the optinal SERVER parameter")
                    max_count = True
                    break
            if max_count != True:

                print(f"{dupe_count} duplicates found")
                print("duplicates found, not accurate enough, consider adding the optinal SERVER parameter")
        else:
            print(f"multiple matches that are not identicle: {player_matches_list}")
            print(f"match found: {player_matches_list[0]}")
    elif len(player_matches_list) == 1:
        print(f"match found: {player_matches_list[0]}")
    else:
        print(f"no good matches found")





#   For unique names can use list matching to find ID
#   




if False:
    SERVER_URL = "https://api.battlemetrics.com/servers"
    SERVER_SEARCH_TERM = "Rustopia EU Main"
    SERVER_PARAMS = {
        "filter[search]":SERVER_SEARCH_TERM,
        "filter[game]":"rust",
        }

    server_request = requests.get(url = SERVER_URL, params = SERVER_PARAMS)
    server_json = server_request.json()
    server_parsed = json.dumps(server_json,indent=4,sort_keys=True)
    server_dict = json.loads(server_parsed)
    send_to_json("server-info.json",server_parsed)


    for i in range(10):
        for y in range(10):
            try:
                server_list.append(server_dict["data"][y]["attributes"]["id"])
                server_list.append(server_dict["data"][y]["attributes"]["ip"])
                server_list.append(server_dict["data"][y]["attributes"]["name"])
            except IndexError:
                exit_loop = True
        try:
            next_link = server_dict["links"]["next"]
            server_links_list.append(next_link)
            server_request = requests.get(url = next_link)
            server_json = server_request.json()
            server_parsed = json.dumps(server_json,indent=4,sort_keys=True)
            server_dict = json.loads(server_parsed)
            send_to_json("server-info.json",server_parsed)
        except KeyError:
            break

        if exit_loop:
            break
    pprint.pprint(server_list,indent=4)

    print(len(server_list))

    pprint.pprint(server_links_list,indent=4)

    server_matches_list = difflib.get_close_matches(SERVER_SEARCH_TERM,server_list,n=10,cutoff=0.5)

    pprint.pprint(server_matches_list)

    print(server_matches_list)

    
end = time.time()
print(end-start)



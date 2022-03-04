import os
import json
import discord






player_id = 70902823

server_id = 660901

stream = os.popen('curl -n https://api.battlemetrics.com/players/'+str(player_id)+'/servers/'+str(server_id))
output = stream.read()
output_dict = json.loads(output)
print(output_dict['data']['attributes']['online'])
import os
import json
import discord
#from selenium import webdriver
#from BeautifulSoup import BeautifulSoup
#70902823
TOKEN = 'OTQ4MTMzMjEyNTQ5NDM1Mzky.Yh3X3Q.W2Fnf5bViPaO5-CZVbt8httCvJA'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} connected sucsessfully')

#https://www.battlemetrics.com/players?filter%5Bsearch%5D=    placeholder    &filter%5BplayerFlags%5D=&sort=score

#https://www.battlemetrics.com/players?filter%5Bsearch%5D=    КакТак         &filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bsearch%5D=  
#    placeholder%20placeholder%20placeholder           &filter%5Bserver%5D%5Bgame%5D=rust&sort=score

#https://www.battlemetrics.com/players?filter%5Bsearch%5D=КакТак&filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bsearch%5D=Rustafied%20EU%20Odd&filter%5Bserver%5D%5Bgame%5D=rust&sort=score





@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(';'):
        if ';checkstatus' in message.content.lower():
            splitMsg = message.content.split()
            id = splitMsg[1]

            player_id = id

            server_id = 660901

            stream = os.popen('curl -n https://api.battlemetrics.com/players/'+str(player_id)+'/servers/'+str(server_id))
            output = stream.read()

            output_dict = json.loads(output)
            if output_dict['data']['attributes']['online'] == True:
                status = "online"
                #comment2
            else:
                status = "offline"
            
            await message.channel.send("User with battlemetrics id of "+ id + " is " + status + " on Rustafied EU Odd")
        #elif ';check'

client.run(TOKEN)
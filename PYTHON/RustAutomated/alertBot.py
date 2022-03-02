import os
import json
import discord
#70902823
from dotenv import load_dotenv
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/Gaming Dator VII/Desktop/Mitt-repo/PYTHON/RustAutomated/chromedriver.exe")


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


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

        if ';checkplayerserver' in message.content.lower():
            
            splitMsg = message.content.split()

            player = splitMsg[1]
            server = splitMsg[2:]

            serverString = ""

            for i in range(len(server)):
                serverString = serverString + server[i]+"%20"

            length = len(serverString)
            serverString = serverString[:length - 3]

            URL = "https://www.battlemetrics.com/players?filter%5Bsearch%5D="+player+"&filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bsearch%5D="+serverString+"&filter%5Bserver%5D%5Bgame%5D=rust&sort=score"
            driver.get(URL)

            element = driver.find_element_by_xpath('//*[@id="PlayerInstancesPage"]/div/ul/li[1]/p/a')

            playerIdLink = element.get_attribute('href')
            
            idLinkSplit = playerIdLink.split("/")

            player_id = idLinkSplit[-1]

            element2 = driver.find_element_by_xpath('//*[@id="PlayerInstancesPage"]/div/ul/li[1]/table/tbody/tr[1]/td[3]/a')
            serverIdLink = element2.get_attribute('href')
            serverLinkSplit = serverIdLink.split("/")

            server_id = serverLinkSplit[-1]

            stream = os.popen('curl -n https://api.battlemetrics.com/players/'+str(player_id)+'/servers/'+str(server_id))
            
            output = stream.read()
            output_dict = json.loads(output)
            if output_dict['data']['attributes']['online'] == True:
                status = "online"
            else:
                status = "offline"

            print(player)
            print(player_id)
            print(status)
            print(server)
            print(server_id)
            serverString = ""
            for ele in server:
                serverString += ele+" "
            print(serverString)

            await message.channel.send("Player "+player+" with a battlemetrics id of: "+player_id+" is currently "+status+" on server "+serverString+" with a battlemetrics id of:"+server_id)


client.run(TOKEN)
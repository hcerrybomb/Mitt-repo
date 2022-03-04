import os
import json
import discord
from pathlib import Path
#70902823
from dotenv import load_dotenv
from selenium import webdriver
from discord.ext import commands, tasks

driver = webdriver.Chrome(executable_path="C:/Users/Gaming_Dator_VII/Desktop/Mitt-repo/python-development/rust-automated/alert-bot/chromedriver.exe")
dotenv_path = Path('C:/Users/Gaming_Dator_VII/Desktop/.env-files/rust-token.env')


#driver = webdriver.Chrome(executable_path="C:/Users/wista002/Desktop/Mitt-repo/python-development/rust-automated/alert-bot/chromedriver.exe")
#dotenv_path = Path('C:/Users/wista002/Desktop/.env-files/rust-token.env')


#https://www.battlemetrics.com/players?filter%5Bsearch%5D=    placeholder    &filter%5BplayerFlags%5D=&sort=score
#https://www.battlemetrics.com/players?filter%5Bsearch%5D=    КакТак         &filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bsearch%5D=  
#    placeholder%20placeholder%20placeholder           &filter%5Bserver%5D%5Bgame%5D=rust&sort=score
#https://www.battlemetrics.com/players?filter%5Bsearch%5D=КакТак&filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bsearch%5D=Rustafied%20EU%20Odd&filter%5Bserver%5D%5Bgame%5D=rust&sort=score
load_dotenv(dotenv_path=dotenv_path)
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=';')
watchlist = []



@bot.event
async def on_ready():
    print(f'{bot.user} connected sucsessfully')
    if not loop_function.is_running():
        loop_function.start()



@tasks.loop(seconds=15)
async def loop_function():
    print("loop run")
    for i in range(len(watchlist)):

        channel = bot.get_channel(692411124616003587)

        player_id = watchlist[i][0]
        server_id = watchlist[i][1]
        player_status = watchlist[i][2]

        stream = os.popen('curl -n https://api.battlemetrics.com/players/'+str(player_id)+'/servers/'+str(server_id))
        output = stream.read()
        output_dict = json.loads(output)
        status = output_dict['data']['attributes']['online']

        if player_status == None:
            if status == True: 
                await channel.send(f"newly added player with id {player_id} is ONLINE on server with id: {server_id}")
            if status == False:           
                await channel.send(f"newly added player with id {player_id} is OFFLINE on server with id: {server_id}")

        if status and watchlist[i][3] == False:
            watchlist[i][3] = True
            watchlist[i][4] = False
            watchlist[i][2] = True
            await channel.send(f"player with id {player_id} has logged ON to server with id: {server_id}")

        if status == False and watchlist[i][4] == False:
            watchlist[i][4] = True
            watchlist[i][3] = False
            watchlist[i][2] = False
            await channel.send(f"player with id {player_id} has logged OFF to server with id: {server_id}")

        print(watchlist[i])

    

@bot.command(name="getWatchlist", help=";getWatchlist \n\nprints the current watchlist")
async def printWatchlist(ctx):
    embedOne = discord.Embed(title="Player Watchlist", description="",color=0x00ff00)
    for i in range(len(watchlist)):
        if watchlist[i][2]==True:
            embedOne.add_field(name=f"Player ID {watchlist[i][0]} ", value=f"is currently ONLINE on server ID {watchlist[i][1]}\n", inline=False)
        else:
            embedOne.add_field(name=f"Player ID {watchlist[i][0]} ", value=f"is currently OFFLINE on server ID {watchlist[i][1]}\n", inline=False)


    await ctx.message.channel.send(embed=embedOne)
    



@bot.command(name="addIdToWatchList", help=";addIdToWatchList <PLayerId> <ServerId> \n\nwhen the id is detected on the given server the bot will alert, updates every 30 seconds")
async def playerWatchList(ctx, *args):

    argsList = list(args)
    playerId = argsList[0]
    serverId = argsList[1]
    playerStatus = None
    onPlayerMsgSent = False
    ofPlayerMsgSent = False
    playerProfile = [playerId,serverId,playerStatus,onPlayerMsgSent,ofPlayerMsgSent]
    watchlist.append(playerProfile)
    print(watchlist)



@bot.command(name="checkPlayerServer", help=";addIdToWatchList <PLayerName> <Server Name> \n\ngets sent to BM site and PlayerName gets searched up with Server Name in server search, very unreliable")
async def playerCheck(ctx):
    if ctx.message.author == bot.user:
        return
    splitMsg = ctx.message.content.split()

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
    fullTitle = ""
    fullTitle = "Status of "+player+" on server "+serverString
    fullDescription="player id: "+player_id+"\n server id: "+server_id
    #https://stackoverflow.com/questions/44862112/how-can-i-send-an-embed-via-my-discord-bot-w-python

    embedOne = discord.Embed(title=fullTitle, description=fullDescription,color=0x00ff00)
    embedOne.add_field(name="Field1", value="Status: "+status, inline=False)

    await ctx.message.channel.send(embed=embedOne)
    #await ctx.message.channel.send("Player "+player+" with a battlemetrics id of: "+player_id+" is currently "+status+" on server "+serverString+" with a battlemetrics id of:"+server_id)


bot.run(TOKEN)
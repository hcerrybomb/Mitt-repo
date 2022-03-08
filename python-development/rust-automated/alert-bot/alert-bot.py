import os
import json
import discord
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from discord.ext import commands, tasks

#driver = webdriver.Chrome(executable_path="C:/Users/Gaming_Dator_VII/Desktop/Mitt-repo/python-development/rust-automated/alert-bot/chromedriver.exe")
#dotenv_path = Path('C:/Users/Gaming_Dator_VII/Desktop/.env-files/rust-token.env')


driver = webdriver.Chrome(executable_path="C:/Users/wista002/Desktop/Mitt-repo/python-development/rust-automated/alert-bot/chromedriver.exe")
dotenv_path = Path('C:/Users/wista002/Desktop/.env-files/rust-token.env')


#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImQ2NzY0ZjU3OTcwY2ZlYmYiLCJpYXQiOjE2NDY1NjU2NTUsIm5iZiI6MTY0NjU2NTY1NSwiaXNzIjoiaHR0cHM6Ly93d3cuYmF0dGxlbWV0cmljcy5jb20iLCJzdWIiOiJ1cm46dXNlcjo1Mjk3NTMifQ.CCAsM9QodXjl1OUi-dqY-PFnv5_2_d6J8eShuNuJ9oQ

#curl -n -X POST https://api.battlemetrics.com/players/match \ -d '{ "data": [ {"type": "identifier", "attributes": {"type": "steamID", "identifier": "76561198313072306" } } ] }' \ -H "Content-Type: application/json" \ -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImQ2NzY0ZjU3OTcwY2ZlYmYiLCJpYXQiOjE2NDY1NjU2NTUsIm5iZiI6MTY0NjU2NTY1NSwiaXNzIjoiaHR0cHM6Ly93d3cuYmF0dGxlbWV0cmljcy5jb20iLCJzdWIiOiJ1cm46dXNlcjo1Mjk3NTMifQ.CCAsM9QodXjl1OUi-dqY-PFnv5_2_d6J8eShuNuJ9oQ"






load_dotenv(dotenv_path=dotenv_path)
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=';')
watchlist = []
watchlist_dict = {}
watchlist_servers = []
channel_id = 692411124616003587

def onlineStatus(PLAYER_ID,SERVER_ID):
    stream          = os.popen('curl -n https://api.battlemetrics.com/players/'+str(PLAYER_ID)+'/servers/'+str(SERVER_ID))
    output          = stream.read()
    output_dict     = json.loads(output)
    print(output_dict)
    print(output_dict['data']['attributes']['online'])
    return output_dict['data']['attributes']['online']

@bot.event
async def on_ready():
    print(f'{bot.user} connected sucsessfully')
    if not loop_function.is_running():
        loop_function.start()



@tasks.loop(seconds=15)
async def loop_function():

    for i in range(len(watchlist_dict)):

        channel     = bot.get_channel(channel_id)

        player_id   = watchlist_dict[i]["PLAYER_ID"]
        server_id   = watchlist_dict[i]["ASSOCIATED_SERVER_ID"]
        online_msg  = watchlist_dict[i]["ON_PLAYER_MSG_SENT"]
        offline_msg = watchlist_dict[i]["OF_PLAYER_MSG_SENT"]

        status      = onlineStatus(player_id,server_id)

        if status and online_msg == False:

            watchlist_dict[i]["ON_PLAYER_MSG_SENT"] = True
            watchlist_dict[i]["OF_PLAYER_MSG_SENT"] = False
            watchlist_dict[i]["PLAYER_STATUS"]      = True

            await channel.send(f"player with id {player_id} has logged ON to server with id: {server_id}")

        if status == False and offline_msg == False:

            watchlist_dict[i]["OF_PLAYER_MSG_SENT"] = True
            watchlist_dict[i]["ON_PLAYER_MSG_SENT"] = False
            watchlist_dict[i]["PLAYER_STATUS"]      = False

            await channel.send(f"player with id {player_id} has logged OFF to server with id: {server_id}")



@bot.command(name="addServerToWatchlist", help=";addServerToWatchlist <name> \n\nadds server to list of servers the watchlist checks")

@bot.command(name="getWatchlist", help=";getWatchlist \n\nprints the current watchlist")
async def getWatchlist(ctx):

    embed_one = discord.Embed(title="Player Watchlist", description="",color=0x00ff00)

    for i in range(len(watchlist_dict)):

        status_string = "ONLINE" if watchlist_dict[i]["PLAYER_STATUS"] else "OFFLINE"

        embed_one.add_field(name=f"Player ID {watchlist_dict[i]['PLAYER_ID']} ", 
        value=f"is currently {status_string} on server ID {watchlist_dict[i]['ASSOCIATED_SERVER_ID']}\n", 
        inline=False)

    await ctx.message.channel.send(embed=embed_one)
    

@bot.command(name="addIdToWatchList", help=";addIdToWatchList <PLayerId> <ServerId> \n\nwhen the id is detected on the given server the bot will alert, updates every 30 seconds")
async def addIdToWatchList(ctx, *args):

    args_list = list(args)

    player_id = args_list[0]
    server_id = args_list[1]

    status = onlineStatus(player_id,server_id)

    watchlist_dict[len(watchlist_dict)] = {

        "PLAYER_ID":player_id,
        "ASSOCIATED_SERVER_ID":server_id,
        "PLAYER_STATUS":status,
        "ON_PLAYER_MSG_SENT":False,
        "OF_PLAYER_MSG_SENT":False

        }

    status_string = "ONLINE" if status else "OFFLINE"

    await ctx.message.channel.send(f"newly added player with id {player_id} is {status_string} on server with id: {server_id}")


#   https://www.battlemetrics.com/players?filter%5Bsearch%5D=    placeholder    &filter%5BplayerFlags%5D=&sort=score
#   https://www.battlemetrics.com/players?filter%5Bsearch%5D=    КакТак         &filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bsearch%5D=  
#   placeholder%20placeholder%20placeholder           &filter%5Bserver%5D%5Bgame%5D=rust&sort=score
#   https://www.battlemetrics.com/players?filter%5Bsearch%5D=КакТак&filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bsearch%5D=Rustafied%20EU%20Odd&filter%5Bserver%5D%5Bgame%5D=rust&sort=score

bot.run(TOKEN)
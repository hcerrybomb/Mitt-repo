from asyncore import poll
import os
from json import loads
from pydoc import describe
import discord #discord.py-message-components
import audioread
from pathlib import Path
from dotenv import load_dotenv #python-dotenv
from discord.ext import commands, tasks 
from discord import Button, ButtonStyle, Embed
from asyncio import sleep

dotenv_path  = Path('C:/Users/Gaming_Dator_VII/Desktop/.env-files/nato-token-2.env')
#dotenv_path = Path('C:/Users/wista002/Desktop/.env-files/nato-token-2.env')

mp3path = r"S:\Random-media\siren.mp3"
#mp3path = r"C:\Users\wista002\Downloads\siren.mp3"


load_dotenv(dotenv_path=dotenv_path)

TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix=";;;")






def parse_embed_json(json_file):
    embeds_json = loads(json_file)['embeds']

    for embed_json in embeds_json:
        embed = Embed().from_dict(embed_json)
        yield embed






@client.event
async def on_message(message):
    interactionChannel = client.get_channel(968800374343483392)
    rulesChannel = client.get_channel(968473733788495943)
    if message.content== ";;;turret-raid":
        await interactionChannel.send("it works 1")
        alarmVoiceChannel = client.get_channel(968467857543426058)
    

    
        vc = await alarmVoiceChannel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/FFmpeg/bin/ffmpeg.exe",source = mp3path))
        with audioread.audio_open(mp3path) as f:
            await sleep(f.duration)
        await vc.disconnect()
    if message.content== ";;;send-vote-embed-1672371":
        print("yes it do")
        with open(r"C:\Users\Gaming_Dator_VII\Desktop\Mitt-repo\python-development\rust-automated\rust-qol\nato-bot\embed.json", "r") as file:
            temp_ban_embeds = parse_embed_json(file.read())
        for embed in temp_ban_embeds:
            await rulesChannel.send(embed=embed)


    if message.content== ";;;send-info-embed-1672371":

        embed = discord.Embed(
            title="**Important!**",
            url="", 
            description="Once you've accepted the rules you'll get access to the #wipe-polls channel, where you can vote yourself into the wipe and you'll get access to the rest of the server",
            color=0xFF5733,
        )
        embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")
        await rulesChannel.send(embed=embed)




    



@client.command(name="printPollInfo")
async def printPoll(ctx):

    pollChannel = client.get_channel(970000977736380548)
    embed = discord.Embed(
        title="Wipe polls",
        url="", 
        description="To join the upcoming wipe submit your info into the poll below and you'll be added and given the @player role",
        color=0xFF5733,
    )
    embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")

    await pollChannel.send(embed=embed)
    await pollChannel.send("https://strawpoll.com/polls/e6Z2e1BkMgN")

@client.event
async def on_ready():
    print(f'{client.user} connected !')

    pollChannel = client.get_channel(970000977736380548)
    embed = discord.Embed(
        title="Wipe polls",
        url="", 
        description="To join the upcoming wipe submit your info into the poll below and you'll be added and given the @player role",
        color=0xFF5733,
    )
    embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")
    await pollChannel.purge()
    await pollChannel.send(embed=embed)
    await pollChannel.send("https://strawpoll.com/polls/e6Z2e1BkMgN")




    embed = discord.Embed(
        title="Next wipe!",
        url="", 
        description="Information regarding the upcoming NATO wipe!"
        +"\n\n\n**When:**\nForced wipe 2/6/2022 @ 20:00 CEST"
        +"\n\n**Server:**\nRustoria EU Medium (?)"
        +"\n\n**Battlemetrics:**\nhttps://www.battlemetrics.com/servers/rust/9594569"
        +"\n\n**Wipes:**\nBi-Weekly on Thursdays @ 3PM UK / 4PM CEST"
        +"\n\n**Connect:**\nconnect 208.103.169.220:28015\n\n",
        color=0xFF5733,

        )
    embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")
    

    wipeChannel = client.get_channel(968442631203999774)
    await wipeChannel.purge()
    await wipeChannel.send(embed=embed)



    embed = discord.Embed(
        title="ALARM",
        url="", 
        description="Press the button under to activate the alarm in the alarm vc",
        color=0xFF5733,

        )
    embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")


    alarmChannel = client.get_channel(968467707202785312)
    await alarmChannel.purge()
    await alarmChannel.send(embed=embed,components=[[
        Button(label="Activate alarm",custom_id="cus1", style=ButtonStyle.red)
    ]])
    


    if False:
        embed = discord.Embed(
            title="Example name: W16",
            url="", 
            description="\n\n**Name here**\nSteam:https://steamcommunity.com/id/SiegeMann/"
            +"\n\n**Name here**\nSteam:https://steamcommunity.com/id/SiegeMann/"
            +"\n\n**Name here**\nSteam:https://steamcommunity.com/id/SiegeMann/"
            +"\n\n**Name here**\nSteam:https://steamcommunity.com/id/SiegeMann/",
            color=0xFF5733,

            )
        embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")


        namesChannel = client.get_channel(968443844607754250)
        await namesChannel.purge()
        await namesChannel.send(embed=embed)

@client.event
async def on_raw_button_click(interaction: discord.Interaction, button):
    print("yea this happens")
    await interaction.respond('Alarm activated! This message will now delete', delete_after=10)
    alarmVoiceChannel = client.get_channel(968467857543426058)
    

    
    vc = await alarmVoiceChannel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/FFmpeg/bin/ffmpeg.exe",source = mp3path))
    with audioread.audio_open(mp3path) as f:
        await sleep(f.duration)
    await vc.disconnect()

client.run(TOKEN)

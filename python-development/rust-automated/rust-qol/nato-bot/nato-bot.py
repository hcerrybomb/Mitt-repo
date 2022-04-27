from http import client
import os
import json
from turtle import dot
import discord
import audioread
from pathlib import Path
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord import Button, ButtonStyle
from asyncio import sleep

dotenv_path  = Path('C:/Users/Gaming_Dator_VII/Desktop/.env-files/nato-token.env')
#dotenv_path = Path('C:/Users/wista002/Desktop/.env-files/nato-token.env')

load_dotenv(dotenv_path=dotenv_path)

TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix=";")



@client.event
async def on_ready():
    print(f'{client.user} connected !')
    embed = discord.Embed(
        title="Next wipe",
        url="", 
        description="Information regarding the upcoming NATO wipe!"
        +"\n\n\n**Server:**\nRustoria EU Medium"
        +"\n\n**Battlemetrics:**\nhttps://www.battlemetrics.com/servers/rust/9594569"
        +"\n\n**Wipe:**\nBi-Weekly on Thursdays @ 3PM UK / 4PM CEST"
        +"\n\n**Connect:**\nconnect 208.103.169.220:28015\n\n",
        color=0xFF5733,

        )
    embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")
    

    wipeChannel = client.get_channel(968442631203999774)
    await wipeChannel.send(embed=embed)






    embed = discord.Embed(
        title="ALARM",
        url="", 
        description="Press the button under to activate the alarm in the alarm vc",
        color=0xFF5733,

        )
    embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")


    alarmChannel = client.get_channel(968467707202785312)
    await alarmChannel.send(embed=embed,components=[[
        Button(label="Activate alarm",custom_id="cus1", style=ButtonStyle.red)
    ]])



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
    await namesChannel.send(embed=embed)

@client.event
async def on_raw_button_click(interaction: discord.Interaction, button):
    print("yea this happens")
    await interaction.respond('Alarm activated! This message will now delete', delete_after=10)
    alarmVoiceChannel = client.get_channel(968467857543426058)
    
    path = r"S:\Random-media\cockroach.mp3"
    vc = await alarmVoiceChannel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/FFmpeg/bin/ffmpeg.exe",source = path))
    with audioread.audio_open(path) as f:
        #Start Playing
        await sleep(f.duration)
    await vc.disconnect()

client.run(TOKEN)

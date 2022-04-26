import os
import json
from turtle import dot
import discord
from pathlib import Path
from dotenv import load_dotenv
from discord.ext import commands, tasks

#dotenv_path  = Path('C:/Users/Gaming_Dator_VII/Desktop/.env-files/nato-token.env')
dotenv_path = Path('C:/Users/wista002/Desktop/.env-files/nato-token.env')

load_dotenv(dotenv_path=dotenv_path)

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=";")

@bot.event
async def on_ready():
    print(f'{bot.user} connected !')
    

bot.run(TOKEN)

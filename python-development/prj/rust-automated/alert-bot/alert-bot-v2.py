import os
import json
import discord
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from discord.ext import commands, tasks

from rustplus import *

options = CommandOptions(prefix="!")

dotenv_path = Path('C:/Users/Gaming_Dator_VII/Desktop/.env-files/rust-token.env')
#dotenv_path = Path('C:/Users/wista002/Desktop/.env-files/rust-token.env')

load_dotenv(dotenv_path=dotenv_path)
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=';')


@bot.event
async def on_ready():
    print(f'{bot.user} connected sucsessfully')
    if not loop_function.is_running():
        loop_function.start()


@tasks.loop(seconds=15)
async def loop_function():
    print("hello world")



bot.run(TOKEN)
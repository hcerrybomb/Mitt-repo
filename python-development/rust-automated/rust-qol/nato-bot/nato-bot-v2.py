import interactions
import os
from dotenv import load_dotenv #python-dotenv
from pathlib import Path
#dotenv_path  = Path('C:/Users/Gaming_Dator_VII/Desktop/.env-files/nato-token.env')
dotenv_path = Path('C:/Users/wista002/Desktop/.env-files/nato-token.env')

load_dotenv(dotenv_path=dotenv_path)

TOKEN = os.getenv('DISCORD_TOKEN')

client = interactions.Client(token = TOKEN)

namesDB = [
    {
        "name":"W16(test)",
        "data":[
            {
              "playername":"SiegeMann",
              "steamlink":"http://steamcommunity.com/id/siegeMann"  
            },
                        {
              "playername":"AndelS",
              "steamlink":"http://steamcommunity.com/id/andels"  
            },
                        {
              "playername":"Kaktak",
              "steamlink":"http://steamcommunity.com/id/kaktak"  
            },
        ]
    },
        {
        "name":"K19(test)",
        "data":[
            {
              "playername":"Sinppa",
              "steamlink":"http://steamcommunity.com/id/sinppa"  
            },
                        {
              "playername":"Larba",
              "steamlink":"http://steamcommunity.com/id/larba"  
            },
                        {
              "playername":"Teddi",
              "steamlink":"http://steamcommunity.com/id/teddi"  
            },
        ] 
    }
]

@client.command(
    name="add player",
    description="add a player profile to database",
    scope=968434095380111391,
    options = [
        interactions.Option(
            name="grid/name",
            description="which group ",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        
    ],
)
async def test(ctx: interactions.CommandContext, text: str):
    await ctx.send(f"You said '{text}'!")





client.start()
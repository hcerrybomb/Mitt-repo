import interactions
import os
from dotenv import load_dotenv #python-dotenv
from pathlib import Path


import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(Path('C:/Users/Gaming_Dator_VII/Desktop/Mitt-repo/python-development/rust-automated/rust-qol/nato-bot/serviceAccountKey.json'))
firebase_admin.initialize_app(cred)

db = firestore.client()
collection = db.collection("nato-db")


dotenv_path  = Path('C:/Users/Gaming_Dator_VII/Desktop/.env-files/nato-token.env')
#dotenv_path = Path('C:/Users/wista002/Desktop/.env-files/nato-token.env')

load_dotenv(dotenv_path=dotenv_path)


TOKEN = os.getenv('DISCORD_TOKEN')

client = interactions.Client(token = TOKEN)


@client.command(
    name="add_player",
    description="add player to database",
    scope=968434095380111391,
    options=[
        interactions.Option(
            name="grid_or_group",
            description="grid or name of the group of the player",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="player_name",
            description="name of the player",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="steam_link",
            description="steam community profile link",
            type=interactions.OptionType.STRING,
            required=False,
        )
    ]
)
async def my_first_command(ctx: interactions.CommandContext, 
    grid_or_group: str, player_name: str, steam_link: str):
    foundGroup = False
    DBdocs = collection.get()
    for i in range(len(DBdocs)):
        if grid_or_group == DBdocs[i].to_dict()['name']:

            updated_array = DBdocs[i].to_dict()['data'] 
            updated_array.append({
                'playername':player_name,
                'steamlink':steam_link
            })
            collection.document(DBdocs[i].id).update({
                'data':updated_array
            })
            foundGroup = True
    if foundGroup == False:
        collection.document(grid_or_group).set({
            'name':grid_or_group,
            'data': [{
                'playername':player_name,
                'steamlink':steam_link
                }
            ]
        }
        )
        
    embed = interactions.Embed(
        title=f"Group: {True}",
        url="", 
        description="\n\n**Name here**\nSteam:https://steamcommunity.com/id/SiegeMann/"
        +"\n\n**Name here**\nSteam:https://steamcommunity.com/id/SiegeMann/"
        +"\n\n**Name here**\nSteam:https://steamcommunity.com/id/SiegeMann/"
        +"\n\n**Name here**\nSteam:https://steamcommunity.com/id/SiegeMann/",
        color=0xFF5733,

        )
    embed.set_thumbnail(url="https://i.imgur.com/eN4wJfL.png")
    await ctx.send(embed= embed)



client.start()
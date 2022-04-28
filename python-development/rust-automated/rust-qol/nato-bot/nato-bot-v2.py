import interactions
import os
from dotenv import load_dotenv #python-dotenv
from pathlib import Path

import discord

import firebase_admin
from firebase_admin import credentials, firestore
from numpy import delete

cred = credentials.Certificate(Path('C:/Users/Gaming_Dator_VII/Desktop/Mitt-repo/python-development/rust-automated/rust-qol/nato-bot/serviceAccountKey.json'))
#cred = credentials.Certificate(Path('C:/Users/wista002/Desktop/Mitt-repo/python-development/rust-automated/rust-qol/nato-bot/serviceAccountKey.json'))

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
async def add_player(ctx: interactions.CommandContext, 
    grid_or_group: str, player_name: str, steam_link: str = "False"):
    
    print(steam_link)

    foundGroup = False
    DBdocs = collection.get()
    for i in range(len(DBdocs)):
        print(DBdocs[i].to_dict())
        prox_dict = DBdocs[i].to_dict()
        print(prox_dict)
        print(prox_dict["name"])
        if grid_or_group == prox_dict['name']:

            updated_array = DBdocs[i].to_dict()['data']
            if steam_link =="False":
                updated_array.append({
                    'playername':player_name,
                    'steamlink':""
                    
                })
            else:
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
    #all_embeds = []
    DBdocs = collection.get()
    await ctx.get_channel()
    await ctx.channel.purge(100, bulk=True)
    await ctx.send("loading database . . .  you can dismiss this message",ephemeral=True)
    thumbnail = interactions.EmbedImageStruct(url="https://i.imgur.com/eN4wJfL.png")._json
    descSTR = "\n**Commands:**\n\n*/add_player*\n**grid_or_group:**  <grid or group name>\n**player_name:**  <player name>\n**steam_link: (optional)**  <link to the players steam account>\n\nsetting **player_name** to the same name as an already existing group will add that player to that group, putting a new group name will create a new group.\n\n\n*/remove_player* \n**group_name:**  <grid or group name>\n**player_index:**  <number index of the player you wish to remove from the database>"
    embed = interactions.Embed(
        title=f"#names info!",
        thumbnail=thumbnail,
        description=descSTR,
        color=0xFF5733,
    )
    await ctx.channel.send(embeds=embed)
    thumbnail = interactions.EmbedImageStruct(url="https://i.imgur.com/eN4wJfL.png")._json
    embed = interactions.Embed(
        title=f"GROUPS:",
        color=0xFF5733,
    )
    await ctx.channel.send(embeds=embed)
    for i in range(len(DBdocs)):
        group_name = DBdocs[i].to_dict()['name']
        names = DBdocs[i].to_dict()['data']
        content = ""
        for j in range(len(names)):
            player_name = names[j]['playername']
            steam_link = names[j]['steamlink']
            content += f"\n\n**{player_name}**     (index: {j})\n{steam_link}"

        thumbnail = interactions.EmbedImageStruct(url="https://i.imgur.com/eN4wJfL.png")._json
        embed = interactions.Embed(
            title=f"Group: {group_name}",
            thumbnail=thumbnail,
            description=content,
            color=0xFF5733,
        )
        #all_embeds.append(embed)
        
        await ctx.channel.send(embeds=embed)
        



client.start()
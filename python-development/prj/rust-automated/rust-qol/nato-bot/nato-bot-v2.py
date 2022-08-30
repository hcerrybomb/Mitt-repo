import interactions
import os
from dotenv import load_dotenv #python-dotenv
from pathlib import Path
import time
import discord

import firebase_admin
from firebase_admin import credentials, firestore


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


#make command @Client.event 3
#async def change_group_name:
#   for i in range(len(DBdocs)):
#       find group name with old_name
#       copy that group with new name   
#       delete old_name group, add new name group       








@client.command(
    name="remove_player",
    description="remove a player from a group",
    scope=968434095380111391,
    options=[
        interactions.Option(
            name="group_name",
            description="exact name of the grid or group",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="player_index",
            description="index of player in group you wish to remove",
            type=interactions.OptionType.INTEGER,
            required=True
        )
    ]
)
async def remove_player(ctx: interactions.CommandContext, group_name: str, player_index: str):

    foundGroup = False
    DBdocs = collection.get()
    for i in range(len(DBdocs)):
        prox_dict = DBdocs[i].to_dict()
        if len(prox_dict['data']) < 1:
            collection.document(DBdocs[i].id).delete()
            prox_dict = DBdocs[i].to_dict()
        if group_name == prox_dict['name']:
            foundGroup = True
            #GROOUP FOUND
            updated_array = DBdocs[i].to_dict()['data']
            try:
                del updated_array[player_index-1]
                collection.document(DBdocs[i].id).update({
                    'data':updated_array
                })

            except IndexError:
                print("index out of range")
                #INDEX OUT OF RAGE
    if foundGroup == False:
        print("dont do anythin")
        await ctx.get_channel()
        await ctx.channel.send("Error: No group matches that name. . . you can dismiss this message", ephemeral=True)
    else:

        DBdocs = collection.get()
        await ctx.get_channel()
        await ctx.channel.purge(100, bulk=True)
        await ctx.send("loading database . . .  you can dismiss this message",ephemeral=True)
        thumbnail = interactions.EmbedImageStruct(url="https://i.imgur.com/eN4wJfL.png")._json
        descSTR = "\n**Commands:**\n\n*/add_player*\n**grid_or_group:**  <grid or group name>\n**player_name:**  <player name>\n**steam_link: (optional)**  <link to the players steam account>\n\nsetting **group_name** to the same name as an already existing group will add that player to that group, putting a new group name will create a new group.\n\n\n*/remove_player* \n**group_name:**  <grid or group name>\n**player_index:**  <number index of the player you wish to remove from the database>"
        embed = interactions.Embed(
            title=f"#names info!",
            thumbnail=thumbnail,
            description=descSTR,
            color=0xFF5733,
        )
        await ctx.channel.send(embeds=embed)
        thumbnail = interactions.EmbedImageStruct(url="https://i.imgur.com/5kFphNT.png")._json
        icon = interactions.EmbedImageStruct(url="https://i.imgur.com/vUTbQ7x.png")._json
        for i in range(len(DBdocs)):
            
            group_name = DBdocs[i].to_dict()['name']
            names = DBdocs[i].to_dict()['data']
            embedx = interactions.Embed(
                title=f"Group: ** ** *{group_name}* **                                                                                                 ** ",
                color=0xBb0404,
                thumbnail=thumbnail
            )
            
            player_embeds = []
            player_embeds.append(embedx)
            

            
            for j in range(len(names)):
                time.sleep(0.1)
                player_name = names[j]['playername']
                steam_link = names[j]['steamlink']             
                embed = interactions.Embed(
                    title=f"**{player_name}**",
                    description=f"**link: **{steam_link}\n**groupname:** {group_name} ** ** ** ** \n**index:** {j+1}",
                    thumbnail=icon
                )
                player_embeds.append(embed)
            await ctx.channel.send(f"\u200b \n",embeds=player_embeds)       
    

            



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

        if len(prox_dict['data']) < 1:
            collection.document(DBdocs[i].id).delete()
            prox_dict = DBdocs[i].to_dict()

        print(prox_dict)
        print(prox_dict["name"])
        if grid_or_group == prox_dict['name']:

            updated_array = DBdocs[i].to_dict()['data']
            if steam_link =="False" or steam_link == False:
                updated_array.append({
                    'playername':player_name,
                    'steamlink':f"not provided . . . **\u200b                 **"
                    
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
    thumbnail = interactions.EmbedImageStruct(url="https://i.imgur.com/5kFphNT.png")._json
    icon = interactions.EmbedImageStruct(url="https://i.imgur.com/vUTbQ7x.png")._json
    for i in range(len(DBdocs)):
        
        group_name = DBdocs[i].to_dict()['name']
        names = DBdocs[i].to_dict()['data']
        embedx = interactions.Embed(
            title=f"Group: ** ** *{group_name}* **                                                                                                 ** ",
            color=0xBb0404,
            thumbnail=thumbnail
        )
        
        player_embeds = []
        player_embeds.append(embedx)
        
        for j in range(len(names)):
            time.sleep(0.1)
            player_name = names[j]['playername']
            steam_link = names[j]['steamlink']             
            embed = interactions.Embed(
                title=f"**{player_name}**",
                description=f"**link: **{steam_link}\n**groupname:** {group_name} ** ** ** ** \n**index:** {j+1}",
                thumbnail=icon
            )
            player_embeds.append(embed)
        await ctx.channel.send(f"\u200b \n",embeds=player_embeds)   

            
        if True:
            for j in range(4, len(names)+4):
                index = j -4
                player_name = names[index]['playername']
                steam_link = names[index]['steamlink']   
                if j % 4 == 0:
                    embed = discord.Embed(
                        title="\u200b",
                        color=0xFF5733
                    )
                    if j > 4:
                        await ctx.channel.send(embeds = interactions.Embed(**embed.to_dict()))
                embed.add_field(name="\u200b",value="** **",inline=False)
                embed.add_field(name=f"{player_name}", value=f"{steam_link}", inline=True)
                embed.add_field(name=f"index:  {j}", value=f"group name: {group_name}", inline=True)
                    
            
        
            if len(names) <= 6:
                for j in range(len(names)):
                    player_name = names[j]['playername']
                    steam_link = names[j]['steamlink']
                    init_embed.add_field(name=f"{player_name}", value=f"{steam_link}", inline=True)
                    
                    init_embed.add_field(name=f"index:  {j}", value=f"group name: {group_name}", inline=True)
                    init_embed.add_field(name="\u200b",value="** **",inline=False)                
                await ctx.channel.send(embeds=interactions.Embed(**init_embed.to_dict()))
            else:
                for x in range(0,6):
                    print("init name added")
                    player_name = names[x]['playername']
                    steam_link = names[x]['steamlink']
                    init_embed.add_field(name=f"{player_name}", value=f"{steam_link}", inline=True)
                    
                    init_embed.add_field(name=f"index:  {x}", value=f"group name: {group_name}", inline=True)
                    init_embed.add_field(name="\u200b",value="** **",inline=False)                
                await ctx.channel.send(embeds=interactions.Embed(**init_embed.to_dict()))
                print("init name sent")
                names_left = len(names)-6 
                
                for j in range(6, len(names)):
                    print("here: 1 going through names")
                    player_name = names[j]['playername']
                    steam_link = names[j]['steamlink']
                    print(f"player: {player_name} link: {steam_link}")
                    if j % 6 == 0:
                        print("here: 2, embed made")
                        embedx = discord.Embed(
                            title="test",
                            color=0xFF5733
                        )
                        if j > 6:
                            print("here: 3, extra embed sent")
                            print(embedx)
                            await ctx.channel.send(embeds=interactions.Embed(**embedx.to_dict()))
                            less_than12 = False
                        else:
                            less_than12 = True
                            print("here:4 embed not sent ")
                    embedx.add_field(name=f"{player_name}", value=f"{steam_link}", inline=True)
                    embedx.add_field(name=f"index:  {x}", value=f"group name: {group_name}", inline=True)
                    print("field added")
                    print(embedx)
                    embedx.add_field(name="\u200b",value="** **",inline=False)
                if less_than12:
                    await ctx.channel.send(embeds=interactions.Embed(**embedx.to_dict()))
        



client.start()
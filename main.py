try:
    import os
    import sys
    import discord
    import time
except ModuleNotFoundError:
     print("Requirements not installed, please either wait for me to install the requirements, or install requirements.txt manually...")
     time.sleep(4)

cmd = 'mode 80,25'
os.system(cmd)

def install(package):
    os.system(f"{sys.executable} -m pip install {package}")

from discord.ext.commands import bot
from discord.ext import commands

try:
    import asyncio
except ModuleNotFoundError:
    install("asyncio")

try:
    import platform
except ModuleNotFoundError:
    install("platform")

try:  
    import colorsys
except ModuleNotFoundError:
    install("colorsys")

try:  
    import pystyle
except ModuleNotFoundError:
    install("pystyle")

try:
    import random
except ModuleNotFoundError:
    install("random")

from pystyle import Colorate, Colors

prefix = "."

client = commands.Bot(command_prefix = prefix, case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()

width = os.get_terminal_size().columns

@client.event
async def on_ready():
    print("")
    print(Colorate.Horizontal(Colors.blue_to_green,f'Logged in as {client.user}'.center(width)))
    print(Colorate.Horizontal(Colors.blue_to_green,f'Commands: [ .userinfo ] | [ .send <content>]'.center(width)))
    print("")
    print(Colorate.Horizontal(Colors.blue_to_green,'Developed by: DEV-S4M - GitHub'.center(width)))
    print(Colorate.Horizontal(Colors.blue_to_green,"--------------------------------------------------------------------------------").center(width))
    print("")

@client.event 
async def on_command_error(ctx, error): 
    await ctx.message.delete()
    if isinstance(error, commands.CommandNotFound): 
      error = getattr(error, 'original', error)
      await ctx.send(f"""```ini\n[ Mass DM - DEV-S4M ]\n\n{error}```""")
      print(Colorate.Horizontal(Colors.red_to_yellow,"[ CMD ] | Command not found"))

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    print(Colorate.Horizontal(Colors.green_to_cyan,"[ CMD ] | userinfo"))
    
@commands.has_permissions(administrator=True)
@client.command(pass_context = True)
async def send(ctx, *, content: str):
        for member in ctx.message.server.members:
            try:
                await ctx.send(member, content)
                await print(Colorate.Horizontal(Colors.green_to_cyan,"[ SEND ] | DM Sent To : {} :white_check_mark:  ".format(member)))
            except:
                await print(Colorate.Horizontal(Colors.red_to_yellow,"[ SEND ] | DM can't Sent To : {} :x: ".format(member)))
                print(Colorate.Horizontal(Colors.green_to_cyan,"[ CMD ] | send"))


client.run("MTA4MjU1ODk2MDg4NTgyOTY0Mg.GlM9iu.jbKZlKUS12nQdEd9qc_-kIOXx6JjP_htjHsBS4")                

# bot.py
import os
import random
from main import *

from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.command(name='test')
async def test(ctx):
    response = "Hello World"
    await ctx.send(response)


@bot.command(name="map")
async def test(ctx):
    print("running")
    await main()
    await ctx.send(file=discord.File('map.png')) 

@bot.command(name="TC")

async def TC(ctx):
   await ctx.send("To find your Tool Cupboards ID, hit it with your rock and check combatlog in the f1 console")

@bot.command(name="upkeep")
async def upkeep(ctx):
    tcCommand = "!TC"
    response = (f"Input Tool Cupboard ID here, if you are unsure on how to do this, use command({tcCommand}): ")

    
    await ctx.send(response)

    userResponse = await bot.wait_for("Message")
    # if userResponse.content.isalpha():
    #     return False

    tcID = int(userResponse.content)
    await main(tcID)

    
    # if tcID != int:
    #     await ctx.send("Incorrect ID format, rerun the command.")
    
    # else:
    #     await ctx.send("TC ID added.")
        
    





    
    
    
bot.run(TOKEN)
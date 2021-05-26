from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.ext.commands import CommandNotFound
from  builtins import any
from discord import Intents
import discord
import requests
import os
import asyncio
import random
import psycopg2
import threading

TOKEN = 'TOKEN'
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)
bot = commands.Bot(command_prefix='!',intents=intents)
bot.remove_command('help')
bot.remove_command('kick')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Unkown command! Use **q$help** for a list of available commands")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"loaded {extension} c(p)og")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"unloaded {extension} c(p)og")

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"reloaded {extension} c(p)og")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print("Sucessfully connected to RedBot!")
    await change_status()

async def change_status():
    statusType=0
    while True:
        if statusType == 0:
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="twitch.tv/Redlumux"))
            statusType = 1
        else:
            await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="twitch.tv/Qloomii"))
            statusType=0
        await asyncio.sleep(60)

#---------RUN--------------
bot.run(TOKEN)

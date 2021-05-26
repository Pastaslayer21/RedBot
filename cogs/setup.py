import discord
from discord.ext import commands
from  builtins import any
from discord import Intents
import requests
import os
import random
import asyncio
import datetime
import psycopg2

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def connectdb(self):
        conn = psycopg2.connect(
        host="HOST",
        database="DATABASE-NAME",
        user="USER",
        password="PASSWIRD") 
        return(conn)

    @commands.command()
    async def setup(self, ctx):
        updateEmbed = discordembed=discord.Embed(title=f"Updated to v{results}", description=f"{ctx.author.name} updated RedBot", color=0xf5e642)
        updateEmbed.add_field(name="Changelog:", value=f"{updated}",inline=False)
        updateEmbed.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/lightly-selected/30/loop-480.png")

def setup(bot):
    bot.add_cog(Setup(bot))

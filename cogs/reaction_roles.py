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

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        emoji = payload.emoji.name
        emoji = "'"+emoji+"'"
        print(f"emoji = {emoji}")
        if message_id == 816761584566665306 and (emoji=="'✅'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='Verified') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)

        if message_id == 823587309915078667 and (emoji=="'🔕'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='Notify') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)

        if (message_id == 822221906073354281) and (emoji=="'🟪'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='purple') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟥'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='red') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟦'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='blue') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟨'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='yellow') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟩'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='green') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟧'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='orange') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'⬜'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='white') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        emoji = payload.emoji.name
        emoji = "'"+emoji+"'"
        if message_id == 816761584566665306 and (emoji=="'✅'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='Verified') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
        if message_id == 823587309915078667 and (emoji=="'🔕'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='Notify') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)


        if (message_id == 822221906073354281) and (emoji=="'🟪'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='purple') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟥'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='red') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟦'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='blue') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟨'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='yellow') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟩'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='green') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'🟧'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='orange') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
        if (message_id == 822221906073354281) and (emoji=="'⬜'"):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            
            role = discord.utils.get(guild.roles, name='white') 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)

def setup(bot):
    bot.add_cog(ReactionRoles(bot))
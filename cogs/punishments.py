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
import math

class Punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def history(self, ctx, target: discord.User):
        last = 0
        connect = self.bot.get_cog("Setup")
        #-----------get total warns----------
        print("adding warn")
        conn = connect.connectdb()
        print("connected")
        command = "insert into "
        c = conn.cursor()
        print("cursored")
        command= "select * from punishments where type='warn'"
        print(command)
        c.execute(command)
        print("executed")
        resultswarn = c.fetchall()
        print(resultswarn)
        conn.commit()
        c.close()
        conn.close()
        #-----------get total kicks----------
        print("adding kicks")
        conn = connect.connectdb()
        print("connected")
        command = "insert into "
        c = conn.cursor()
        print("cursored")
        command= "select * from punishments where type='kick'"
        print(command)
        c.execute(command)
        print("executed")
        resultskick = c.fetchall()
        print(resultskick)
        conn.commit()
        c.close()
        conn.close()
        #-----------get total bans----------
        print("adding bans")
        conn = connect.connectdb()
        print("connected")
        command = "insert into "
        c = conn.cursor()
        print("cursored")
        command= "select * from punishments where type='ban'"
        print(command)
        c.execute(command)
        print("executed")
        resultsban = c.fetchall()
        print(resultsban)
        conn.commit()
        c.close()
        conn.close()
        print("Gotten all punishments")
        #-----------doing the message-----------
        warnpages = []
        total_page = discord.Embed (
            title = f'All punishments for {target.name}',
            description = f'React to open up logs for each punishment\n\n**Total Warns:** {len(resultswarn)}\n\n**Total Kicks:** {len(resultskick)}\n\n**Total Bans:** {len(resultsban)}\n',
            colour = 0x00ff00
        )
        print("total page set")

        warn_page = discord.Embed (
            title = f'All warns for {target.name}',
            description = f'React with back to return to main page',
            colour = 0x00ff00
        )
        print("results going")
        print(len(resultswarn))
        if len(resultswarn)<=5:
            print("less then 5")
            for i in range(len(resultswarn)):
                print(resultswarn[i][2])
                mod = await self.bot.fetch_user(resultswarn[i][2])
                print(mod)
                warn_page.add_field(name=f"Warn issued by {mod} || Status: {resultswarn[i][5]}", value=f"reason: {resultswarn[i][4]}\nissued: {resultswarn[i][6]}", inline=False)
                print("added a field")
        elif len(resultswarn)>5:
            print("its > 5  || 0-0")
            warn_pages=[]
            total = len(resultswarn)/5
            total = math.ceil(total)
            print(total)
            for i in range(total):
                print(last)
                print("running")
                locals()["warnpage"+str(i)] = discord.Embed (
                    title = f'All warns for {target.name}',
                    description = f'React with back to return to main page',
                    colour = 0x00ff00
                )
                print(f"total i = {i}")
                print("set an embed")
                print(last)
                for last in range(last+5):
                    print("setting the fields")
                    mod = await self.bot.fetch_user(resultswarn[i][2])
                    print(mod)
                    locals()["warnpage"+str(i)].add_field(name=f"Warn issued by {mod}\nReason: {resultswarn[last][4]}", value=f"Status: {resultswarn[last][5]}\nissued: {resultswarn[last][6]}", inline=False)
                    print("set a field")
                    print(f"{mod} || {resultswarn[last][4]} || {resultswarn[last][5]} || {resultswarn[last][6]}")
                    print(f"last = {last}")

                last = last
                print(last)
                print("appended 1")
                warnpages.append(locals()["warnpage"+str(i)])
                print(locals()["warnpage"+str(i)])


                
            
            print(warnpages)                        

        message = await ctx.send(embed = total_page)
        print("sent")

        await message.add_reaction('🇼')
        await message.add_reaction('🇰')
        await message.add_reaction('🇧')
        

        def check(reaction, user):
            return user == ctx.author

        i = 0
        reaction = None

        while True:
            if str(reaction) == '🇼':
                if len(resultswarn) <= 5:
                    await message.edit(embed = warn_page)
                    await message.add_reaction('⬅️')
                elif len(resultswarn) > 5:
                    await message.edit(embed = warnpages[0])
                    await message.add_reaction('⬅️')
                    await message.add_reaction('▶')
                    atwarnpage = True
            # elif str(reaction) == '🇰':
            #     await message.edit(embed = pages[i])
            #     await message.add_reaction('◀')
            #     await message.add_reaction('▶')
            # elif str(reaction) == '🇧':
            #     await message.edit(embed = pages[i])
            #     await message.add_reaction('◀')
            #     await message.add_reaction('▶')
            elif str(reaction) == '⬅️':
                await message.edit(embed = total_page)
                await message.add_reaction('🇼')
                await message.add_reaction('🇰')
                await message.add_reaction('🇧')
            elif str(reaction) == '◀':
                if i == 0 and atwarnpage == True:
                    await message.edit(embed = warnpages[i-1])
                    await message.add_reaction('▶')
                    await message.add_reaction('⬅️')
                    i = i-1
                    print(i)
            elif str(reaction) == '▶':
                if atwarnpage == True:
                    print(total)
                    i = i+1
                    print(i)
                    await message.edit(embed = warnpages[i])
                    print(warnpages[i])
                    if i == total:
                        await message.add_reaction('◀')
                        await message.add_reaction('⬅️')
                    else:
                        await message.add_reaction('◀')
                        await message.add_reaction('▶')
                        await message.add_reaction('⬅️')

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout = 120.0, check = check)
                await message.remove_reaction(reaction, user)
            except:
                break
            await message.clear_reactions()
        

        



    @commands.command()
    async def warn(self, ctx, target: discord.User,*, reason: str):
        connect = self.bot.get_cog("Setup")
        #-----------get total warns----------
        print("adding warn")
        conn = connect.connectdb()
        print("connected")
        command = "insert into "
        c = conn.cursor()
        print("cursored")
        command= "select * from punishments where type='warn'"
        print(command)
        c.execute(command)
        print("executed")
        results = c.fetchall()
        print(results)
        conn.commit()
        c.close()
        conn.close()
        #-----------auto-mod shit here----------
        #-----------add warn if no auto-mod shit-------
        #ADD IF NO AUTO MOD HERE
        conn = connect.connectdb()
        c = conn.cursor()
        print("connected")
        command = f"""INSERT INTO punishments(user_id, mod_id, "type","reason", "status", "time_issued") VALUES ({target.id},{ctx.author.id},'warn', '{reason}','active', '{datetime.datetime.now().strftime("%m-%d-%Y at %H:%M")}');"""
        print(command)
        c.execute(command)
        print("executed")
        conn.commit()
        c.close()
        conn.close()
        warnmessage = discord.Embed(title=f"User {target.name} has been warned", color=0xf54242)
        warndm = f"""You've been warned in {ctx.guild.name} for "{reason}" """
        await target.send(warndm)
        await ctx.send(embed=warnmessage)


    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def mute(self, ctx, user: discord.Member):
    #     role_name = 'Text Mute'
    #     guild = self.bot.get_guild(530284930119499776)
    #     role = discord.utils.get(guild.roles, name=role_name)
    #     await user.add_roles(role)
    #     await ctx.send(f"User {user} has been silenced!")
    #     await logger(command=f"Muted {user} in all text channels", user=ctx.author, channel=ctx.channel, color="#5e0202", guild=ctx.punishmessage.guild.id)

    # @mute.error
    # async def clear_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send("You cant do that!")
    #         await logger(command=f"Tried to mute {user} in all text channels but lacks permission", user=ctx.author, channel=ctx.channel, color="#f00000", guild=ctx.punishmessage.guild.id)

    # #-----------------------------------------------------------------------
    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def unmute(self, ctx, user: discord.Member):
    #     role_name = 'Text Mute'
    #     guild = self.bot.get_guild(530284930119499776)
    #     role = discord.utils.get(guild.roles, name=role_name)
    #     await user.remove_roles(role)
    #     await ctx.send(f"User {user} can type again!")
    #     await logger(command=f"Unmuted {user} in all text channels", user=ctx.author, channel=ctx.channel, color="#00ff08", guild=ctx.punishmessage.guild.id)

    # @unmute.error
    # async def clear_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send("You cant do that!")
    #         await logger(command=f"Tried to unmute {user} in all text channels but lacks permission", user=ctx.author, channel=ctx.channel, color="#f00000", guild=ctx.punishmessage.guild.id)

    # #-----------------------------------------------------------------------
    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def vcmute(self, ctx, user: discord.Member):
    #     role_name = 'VC Mute'
    #     guild = self.bot.get_guild(530284930119499776)
    #     role = discord.utils.get(guild.roles, name=role_name)
    #     await user.add_roles(role)
    #     await ctx.send(f"User {user} can no longer speak!")
    #     await logger(command=f"Muted {user} in all VCs", user=ctx.author, channel=ctx.channel, color="#5e0202", guild=ctx.punishmessage.guild.id)

    # @vcmute.error
    # async def clear_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send("You cant do that!")
    #         await logger(command=f"Tried mute {user} in all VCs but lacks permission", user=ctx.author, channel=ctx.channel, color="#f00000", guild=ctx.punishmessage.guild.id)

    # #-----------------------------------------------------------------------
    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def vcunmute(self, ctx, user: discord.Member):
    #     role_name = 'VC Mute'
    #     guild = self.bot.get_guild(530284930119499776)
    #     role = discord.utils.get(guild.roles, name=role_name)
    #     await user.remove_roles(role)
    #     await ctx.send(f"User {user} can speak again!")
    #     await logger(command=f"Unmuted {user} in all VCs", user=ctx.author, channel=ctx.channel, color="#00ff08", guild=ctx.punishmessage.guild.id)

    # @vcunmute.error
    # async def clear_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send("You cant do that!")
    #         await logger(command=f"Tried to unmute {user} in all VCs but lacks permission", user=ctx.author, channel=ctx.channel, color="#f00000", guild=ctx.punishmessage.guild.id)

    # #-----------------Kick/Ban-------------------------
    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def kick(self, ctx, user: discord.Member, *, reason="No reason provided"):
    #         await user.kick(reason=reason)
    #         kick = discord.Embed(title=f" Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", color=0xff4a4a)
    #         await ctx.channel.send(embed=kick)
    #         await user.send(embed=kick)
    #         await logger(command=f"Kicked {user} with reason {reason}", user=ctx.author, channel=ctx.channel, color="#5e0202", guild=ctx.punishmessage.guild.id)

    # @kick.error
    # async def clear_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send("You cant do that!")
    #         await logger(command=f"Tried to kick {user} with reason {reason} but lacks permission", user=ctx.author, channel=ctx.channel, color="#f00000", guild=ctx.punishmessage.guild.id)

    # #-----------------------------------------------------------------------
    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def ban(self, ctx, user: discord.Member, *, reason="No reason provided"):
            
    #         await user.ban(reason=reason)
    #         ban = discord.Embed(title=f" Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", color=0xff0000)
    #         await ctx.channel.send(embed=ban)
    #         await user.send(embed=ban)
    #         await logger(command=f"Banned {user} with reason {reason}", user=ctx.author, channel=ctx.channel, color="#5e0202", guild=ctx.punishmessage.guild.id)

    # @ban.error
    # async def clear_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send("You cant do that!")
    #         await logger(command=f"Tried to ban {user} with reason {reason} but lacks permission", user=ctx.author, channel=ctx.channel, color="#f00000", guild=ctx.punishmessage.guild.id)

def setup(bot):
    bot.add_cog(Punishments(bot))
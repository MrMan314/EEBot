import os
import random as rd
import discord
import pytz
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime

TOKEN = os.getenv('DISCORD_TOKEN')

client = Bot("^")
os.chdir("bot")
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ltr = ['A', 'B', 'C', 'D', 'E', 'F']


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


class Information(commands.Cog):

    """Informational Commands"""

    @commands.command()
    async def ctime(self, ctx, tz="UTC"):
        """Tells you the current time of day in a timezone[tz], tz is default UTC"""
        dt = datetime.now(pytz.timezone(tz))
        await ctx.send(rd.choice(["It's ", "The current time is: ", "Here's The time: ",
                                  "BING BONG BING BONG who's your friend who likes to play?  "]) + dt.strftime(
            "%Y-%m-%d %H:%M:%S.%f") + " " + tz)


client.add_cog(Information(client))


class Fun(commands.Cog):

    """Commands for all your FUN needs!"""

    @commands.command()
    async def worm(self, ctx, length=10):
        """Makes a worm a random length from 0 to length, length is set to 10 if not defined"""
        if length < 0:
            await ctx.send("Worm cannot be a negative length, YOU DESTROYED THE UNIVERSE WITH A BLACK HOLE",
                           file=discord.File("blackhole.gif"))
        elif length <= 64:
            await ctx.send("<:wormhead:787786964295614495>" + (
                        "<:wormbody:787786942312874006>" * rd.randint(0, length) + "<:wormtail:787786975703728208>"))
        else:
            await ctx.send("Worm too long, died because it couldn't move!")
            await ctx.send(
                "<:deadwormhead:788823709154148384>  <:wormbody:787786942312874006> <:wormbody:787786942312874006><:wormbody:787786942312874006><:wormbody:787786942312874006> <:wormbody:787786942312874006>  <:wormtail:787786975703728208>")

    @commands.command()
    async def joke(self, ctx):
        """A joke-telling command to joke around"""
        j = open('./joke', 'r')
        jLines = j.readlines()
        jDat = []
        for line in jLines:
            jDat.append(line.strip().split("±"))
        joke = rd.choice(jDat)
        await ctx.send(joke[0])
        try:
            await ctx.send(joke[1])
        except discord.errors.HTTPException:
            pass

    @commands.command()
    async def genkey(self, ctx):
        """Sends you a random 20-digit hexadecimal key, has a 1 in 2001 chance of winning"""
        await ctx.author.create_dm()
        key = str('Key: ||`' +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
                  '`||')
        if rd.randint(-1000, 1000) == 0:
            f = open("winkeys", "a")
            f.write(key + '\n')
        await ctx.author.dm_channel.send(key)
        await ctx.send("Key has successfully been sent")


client.add_cog(Fun(client))


class Audio(commands.Cog):
    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


client.add_cog(Audio(client))


@client.listen('on_message')
async def onMessage(message):
    dt = datetime.now(pytz.timezone("UTC"))
    f = open("new.log", "a")
    f.write("[" + dt.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC] : " + str(message.guild) + " #" + str(
        message.channel) + " - " + str(
        message.author) + ": " + message.content + "\n")
    f.close()
    print(str(message.guild) + " #" + str(message.channel) + " - " + str(
        message.author) + ": " + message.content)
    eq = open('eq', 'r')
    eqLines = eq.readlines()
    eqDat = []
    for line in eqLines:
        eqDat.append(line.strip().split("±"))
    sw = open('sw', 'r')
    swLines = sw.readlines()
    swDat = []
    for line in swLines:
        swDat.append(line.strip().split("±"))
    ew = open('ew', 'r')
    ewLines = ew.readlines()
    ewDat = []
    for line in ewLines:
        ewDat.append(line.strip().split("±"))
    ct = open('ct', 'r')
    ctLines = ct.readlines()
    ctDat = []
    for line in ctLines:
        ctDat.append(line.strip().split("±"))
    if message.author == client.user:
        return
    for data in eqDat:
        if data[0].split("·").__contains__(message.content.lower()):
            await message.channel.send(rd.choice(data[1].split("·")))
    for data in swDat:
        for item in data[0].split("·"):
            if message.content.lower().startswith(item):
                await message.channel.send(rd.choice(data[1].split("·")))
    for data in ewDat:
        for item in data[0].split("·"):
            if message.content.lower().endswith(item):
                await message.channel.send(rd.choice(data[1].split("·")))
    for data in ctDat:
        for item in data[0].split("·"):
            if message.content.lower().__contains__(item):
                await message.channel.send(rd.choice(data[1].split("·")))


client.run(TOKEN)

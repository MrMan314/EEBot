import os
import random as rd
import discord
import pytz
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound
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
    if isinstance(error, CommandNotFound):
        await ctx.send("Error: " + str(error))
        return
    await ctx.send("Error: " + str(error))
    raise error


@client.command()
async def ctime(ctx):
    dt = datetime.now(pytz.timezone("UTC"))
    await ctx.send(rd.choice(["It's ", "The current time is: ", "Here's The time: ",
                              "BING BONG BING BONG who's your friend who likes to play?  "]) + dt.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC")


@client.command()
async def joke(ctx):
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


@client.command()
async def genkey(ctx):
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


@client.listen('on_message')
async def onMessage(message):
    dt = datetime.now(pytz.timezone("UTC"))
    f = open("new.log", "a")
    f.write("[" + dt.strftime("%Y-%m-%d %H:%M:%S.%f") + " GMT] : " + str(message.guild) + " #" + str(message.channel) + " - " + str(
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
    worm_spellings = ["worm", "owrm", "rwom", "wrom", "orwm", "rowm", "mowr", "omwr", "wmor", "mwor", "owmr", "womr", "wrmo", "rwmo", "mwro", "wmro", "rmwo", "mrwo", "mrow", "rmow", "omrw", "morw", "romw", "ormw"]
    if message.author == client.user:
        return
    elif worm_spellings.__contains__(message.content.lower().split(" ")[0]):
        try:
            if int(message.content.lower().split(" ")[1]) <= 1000:
                await message.channel.send("<:wormhead:787786964295614495>" + (
                            "<:wormbody:787786942312874006>" * rd.randint(0, int(
                        message.content.lower().split(" ")[1]))) + "<:wormtail:787786975703728208>")
            else:
                await message.channel.send("Worm too long, died because it couldn't move!")
        except:
            await message.channel.send("<:wormhead:787786964295614495>" + (
                        "<:wormbody:787786942312874006>" * rd.randint(0, 10)) + "<:wormtail:787786975703728208>")
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

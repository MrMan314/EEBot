import os
import random as rd
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
os.chdir("bot")

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
async def on_message(message):
    eq = open('./eq', 'r')
    eqLines = eq.readlines()
    eqDat = []
    for line in eqLines:
        eqDat.append(line.strip().split("±"))
    sw = open('./sw', 'r')
    swLines = sw.readlines()
    swDat = []
    for line in swLines:
        swDat.append(line.strip().split("±"))
    ew = open('./ew', 'r')
    ewLines = ew.readlines()
    ewDat = []
    for line in ewLines:
        ewDat.append(line.strip().split("±"))
    ct = open('./ct', 'r')
    ctLines = ct.readlines()
    ctDat = []
    for line in ctLines:
        ctDat.append(line.strip().split("±"))
    j = open('./joke', 'r')
    jLines = j.readlines()
    jDat = []
    for line in jLines:
        jDat.append(line.strip().split("±"))
    worm_spellings = ["worm", "owrm", "rwom", "wrom", "orwm", "rowm", "mowr", "omwr", "wmor", "mwor", "owmr", "womr", "wrmo", "rwmo", "mwro", "wmro", "rmwo", "mrwo", "mrow", "rmow", "omrw", "morw", "romw", "ormw"]
    if message.author == client.user:
        return
    if message.content.lower().startswith("^say"):
        await message.channel.send(str(message.author) + ": " + message.content[4:2000])
    elif message.content.lower().startswith("^talk"):
        await message.channel.send(str(message.author) + ": " + message.content[5:2000], tts=True)
    elif message.content.lower().startswith("what time is it") or message.content.lower().startswith("^ctime"):
        await message.channel.send(rd.choice(["It's ", "The current time is: ", "Here's The time: ",
                                              "BING BONG BING BONG who's your friend who likes to play?  "]) + str(
            message.created_at) + " GMT")
    elif worm_spellings.__contains__(message.content.lower().split(" ")[0]):
        try:
            await message.channel.send("<:wormhead:756607485800087583>"+("<:wormbody:756607472436773005>"*rd.randint(0, int(message.content.lower().split(" ")[1])))+"<:wormtail:756607453910663208>")
        except:
            await message.channel.send("<:wormhead:756607485800087583>" + ("<:wormbody:756607472436773005>" * rd.randint(0, 10)) + "<:wormtail:756607453910663208>")
    elif message.content.lower().startswith("^emoji"):
        try:
            await message.channel.send(str(message.author) + ": " + message.content[6:2000].replace("«", "<").replace("»", ">"))
        except:
            await message.channel.send("Error Sending Emoji")
    elif ["^joke", "tell me a joke"].__contains__(message.content.lower()):
        joke = rd.choice(jDat)
        await message.channel.send(joke[0])
        try:
            await message.channel.send(joke[1])
        except discord.errors.HTTPException:
            pass
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

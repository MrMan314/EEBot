import os
import random as rd
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
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
async def on_message(message):
    if message.content.lower() == "^genkey":
        await message.author.create_dm()
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
            f.write(key+'\n')
        await message.author.dm_channel.send(key)
        await message.channel.send("Key has successfully been sent")


client.run(TOKEN)

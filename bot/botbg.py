import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    while 1:
        # try:
        channel = client.get_channel(int(input("ChannelID: ")))
        await channel.send(input("Message: "))
        # except:
        #     print("Error Sending Message")

client.run(TOKEN)

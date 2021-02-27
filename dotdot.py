# bot.py
import os
import subprocess
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    if message.author.bot:
        return

    if message.content[:6] == ":print":
        tempy = message.content[6:]
        with open("/dev/usb/lp0","w") as outFile:
            subprocess.run(["echo", tempy],stdout=outFile)
        await message.channel.send("printing this on nick's printer")

client.run(TOKEN)

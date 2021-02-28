# bot.py
import os
import subprocess
import discord
from dotenv import load_dotenv
from texttofont import word_to_ascii

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
"""function chunks from ned batchelder on stackoverflow"""


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content[:7] == ":printf":
        tempy = message.content[6:]
        if tempy[0] == ' ':
            tempy = tempy[1:]
        tempy = word_to_ascii(tempy)
        tempy = message.author.nick + ':\n' + tempy
        chunked = chunks(tempy, 85)
        with open("/dev/usb/lp0", "w") as outFile:
            for line in chunked:
                subprocess.run(["echo", line], stdout=outFile)
        await message.channel.send("printing atof...")

    elif message.content[:6] == ":print":
        tempy = message.content[6:]
        if tempy[0] == ' ':
            tempy = tempy[1:]
        tempy = message.author.nick + ' said: ' + tempy
        chunked = chunks(tempy, 85)
        with open("/dev/usb/lp0", "w") as outFile:
            for line in chunked:
                subprocess.run(["echo", line], stdout=outFile)
        await message.channel.send("printing...")

client.run(TOKEN)

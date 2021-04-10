import discord
import os
from datetime import date
import time
from random import randint
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('prefix is qd.')

@client.event
async def on_message(message):
    today = date.today()
    day = today.strftime("%m/%d/%y")
    password = []
    if message.author == client.user:
        return

    if message.content.startswith("qd.coin"):
        await message.channel.send("How many times do you want to flip the coin?")

        msg = await client.wait_for('message')
#-------------------------------------------------------
        num = msg.content
        num = int(num)
        flips = [randint(0,1) for r in range(num)]
        results = []
        for object in flips:
          if object == 0:
            results.append('Heads')
          elif object == 1:
            results.append('Tails')
        print(results)
        await message.channel.send(results)


keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
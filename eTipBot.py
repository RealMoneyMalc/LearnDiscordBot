import discord
import os
from datetime import date
import time
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('prefix is e.')

@client.event
async def on_message(message):
    if message.content.startswith("e.tip"):
        low = 0.10
        med = 0.15
        high = 0.20
        total = 0
        await message.channel.send("Enter a price:")
        msg = await client.wait_for('message')
        price = msg.content
        price = int(price)


#-------------------------------------------------
        await message.channel.send("Do you want to have a `high`, `med`, or `low` tip?")
        msg = await client.wait_for('message')
        tipsett = msg.content
#-------------------------------------------------
        if tipsett == 'high': #20%
          total = (price * high) + price
          await message.channel.send(total)
        if tipsett == 'med': #15%
          total = (price * med) + price
          await message.channel.send(total)
        if tipsett == 'low': #15%
          total = (price * low) + price
          await message.channel.send(total)









keep_alive()

token = os.environ.get("TOKEN")
client.run(token)
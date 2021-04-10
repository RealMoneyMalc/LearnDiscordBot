import discord
import os
from datetime import date
import time
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('prefix is cv.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("cv.toF"):
        await message.channel.send("Converting Celcius to Fahrenheit")
        await message.channel.send("Input a Celcius temperature:")
        msg = await client.wait_for('message')
        celsius = msg.content
        celsius = int(celsius)
        fahrenheit = (celsius * 1.8) + 32
        await message.channel.send('%0.1f degrees Celsius is equal to %0.1f degrees Fahrenheit' %(celsius,fahrenheit))
#----------------------------------------------------------------------------
    if message.content.startswith("cv.toC"):
        await message.channel.send("Converting Fahrenheit to Celsius")
        await message.channel.send("Input a Fahrenheit temperature:")
        msg = await client.wait_for('message')
        fahrenheit = msg.content
        fahrenheit = int(fahrenheit)
        celsius = (fahrenheit - 32) * 0.555
        await message.channel.send('%0.1f degrees Fahrenheit is equal to %0.1f degrees Celsius' %(fahrenheit,celsius))

#--------------------------------------------------------------------
keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
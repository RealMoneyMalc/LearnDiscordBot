import discord
import os
from datetime import date
from keep_alive import keep_alive
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('prefix is math.')

@client.event
async def on_message(message):
    today = date.today()
    day = today.strftime("%m/%d/%y")
    if message.author == client.user:
        return

    if message.content.startswith("math.function"):
        await message.channel.send("```The function of this bot is to execute simple math calculations. Use math. to issue commands. You can do math.add, math.sub, math.mult, and math.div to calculate the result of two numbers.```")

#-----------------------------------------
#-----------------------------------------
    if message.content.startswith('math.add'):
        numlist = [0]
        channel = message.channel
        await channel.send('Input first number:')
        
        msg = await client.wait_for('message')
        await channel.send("Input second number:")
        numlist.append(msg.content)
        msg = await client.wait_for('message')
        await channel.send("Answer:")
        numlist.append(msg.content)
#-----------------------------------------
        print(numlist)
        numlist[1] = int(numlist[1])
        numlist[2] = int(numlist[2])
        print(numlist)
        tot = sum(numlist)
        print(tot)
        await channel.send(tot)

#-----------------------------------------
#-----------------------------------------
    if message.content.startswith('math.sub'):
        channel = message.channel
        await channel.send('Input first number:')
        numlist = [0]
        msg = await client.wait_for('message')
        await channel.send("Input second number:")
        numlist.append(msg.content)
        msg = await client.wait_for('message')
        await channel.send("Answer:")
        numlist.append(msg.content)
#-----------------------------------------
        print(numlist)
        numlist[1] = int(numlist[1])
        numlist[2] = int(numlist[2])
        print(numlist)
        tot = numlist[1] - numlist[2]
        print(tot)
        await channel.send(tot)

#-----------------------------------------
#-----------------------------------------
    if message.content.startswith('math.mult'):
        channel = message.channel
        await channel.send('Input first number:')
        numlist = [0]
        msg = await client.wait_for('message')
        await channel.send("Input second number:")
        numlist.append(msg.content)
        msg = await client.wait_for('message')
        await channel.send("Answer:")
        numlist.append(msg.content)
#-----------------------------------------
        print(numlist)
        numlist[1] = int(numlist[1])
        numlist[2] = int(numlist[2])
        print(numlist)
        tot = numlist[1] * numlist[2]
        print(tot)
        await channel.send(tot)

#-----------------------------------------
#-----------------------------------------
    if message.content.startswith('math.div'):
        channel = message.channel
        await channel.send('Input first number:')
        numlist = [0]
        msg = await client.wait_for('message')
        await channel.send("Input second number:")
        numlist.append(msg.content)
        msg = await client.wait_for('message')
        await channel.send("Answer:")
        numlist.append(msg.content)
#-----------------------------------------
        print(numlist)
        numlist[1] = int(numlist[1])
        numlist[2] = int(numlist[2])
        print(numlist)
        tot = numlist[1] / numlist[2]
        print(tot)
        await channel.send(tot)




       








keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
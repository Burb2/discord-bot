import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
    	await client.send_message(message.channel, 'toast')
    elif message.content.startswith('!ajoutepunchline'):
    	if not os.path.isfile("punchlines.pk1"):
    		quote_list = []
    	else:
    		with open("punchlines.pk1", "rb") as punchlines:
    			quote_list = pickle.load(punchlines)
    	quote_list.append(message.content[16:])
    	with open("punchlines.pk1", "wb") as punchlines:
    		pickle.dump(quote_list, punchlines)
    elif message.content.startswith("!b2o"):
    	with open("punchlines.pk1", "rb") as punchlines:
    		quote_list = pickle.load(punchlines)
    	await client.send_message(message.channel, random.choice(quote_list))

client.run('Mzk1NjU3MzExODA2MjkxOTc0.DSWzOg.RvA0cReM0m6PSFf4yu1AaM8AB2E')
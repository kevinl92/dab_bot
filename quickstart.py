import discord
import os
from dotenv import load_dotenv
import logging
import random

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

#f = open("links.txt").read().splitlines()

number = 0

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print('ADMIN_ID = ' + os.environ['ADMIN_ID'])
    print('ADMIN_DM = ' + os.environ['ADMIN_DM'])

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(message.author.id)
    print(message.channel.id)
    print (message.author.id == int(os.environ['ADMIN_ID']))
    print (message.channel.id == int(os.environ['ADMIN_DM']))

    if message.author.id == int(os.environ['ADMIN_ID']) and message.channel.id == int(os.environ['ADMIN_DM']):
        await message.channel.send('I can tell this was a DM.')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if "dab" in message.content.lower():
        await message.channel.send(random.choice(open("links.txt").read().splitlines()))

client.run(os.environ['BOT_TOKEN'], log_handler=handler, log_level=logging.DEBUG)
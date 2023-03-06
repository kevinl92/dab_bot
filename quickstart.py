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

f = open("links.txt").read().splitlines()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        #await message.reply('Hello!')

    if "dab" in message.content.lower():
        await message.channel.send(random.choice(f))

client.run(os.environ['BOT_TOKEN'], log_handler=handler, log_level=logging.INFO)
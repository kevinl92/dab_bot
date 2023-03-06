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

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore any message that originated from this bot to prevent looping
    if message.author == client.user:
        return

    # Create admin for future sending?
    admin = await client.fetch_user(os.environ['ADMIN_ID'])

    # If the message came from a DM...
    if message.channel.type.name == 'private': 
        print('DM from '+ message.author.name + ' : ' + message.content)
        if message.author.id == int(os.environ['ADMIN_ID']):
            await message.channel.send('This was a DM from the Admin.')

        else:
            await message.channel.send(message.author.name + ', you aren\'t an admin! We\'ll pass your message along to Arfa.')
            await admin.send(message.author.name + ' DMed Dab_Bot: ' + message.content)

   # Otherwise, this came from a server...
    elif message.channel.type.name == 'text':
        print (message.guild.name + '/' + message.author.name + ':' + message.content)

        # If the message contains the word 'dab', case insensitive
        if "dab" in message.content.lower():
            await message.channel.send(random.choice(open("links.txt").read().splitlines()), delete_after=5.0)
    
    # Otherwise, this is from a source we don't know about and don't know how to handle
    else:
        print ('Unknown origin: ' + message.content)
        return

client.run(os.environ['BOT_TOKEN'], log_handler=handler, log_level=logging.DEBUG)
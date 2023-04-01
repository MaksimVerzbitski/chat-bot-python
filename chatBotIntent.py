import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send(f'Hello, {message.author.mention}!')

        if message.content.startswith('!roll'):
            dice_roll = random.randint(1, 6)
            await message.channel.send(f'{message.author.mention} rolled a {dice_roll}!')

        if message.content.startswith('!quote'):
            response = requests.get('https://api.quotable.io/random')
            if response.status_code == 200:
                data = response.json()
                await message.channel.send(f'{data["content"]} - {data["author"]}')
            else:
                await message.channel.send('Sorry, I could not retrieve a quote at this time.')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)


""" # Basic stuff to start bot

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        if True:
            print(f'Logged on as {self.user}!')
        else:
            print(f'Kurwa')


    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print('\n My name is Johnny Bravo in sandals')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token) """


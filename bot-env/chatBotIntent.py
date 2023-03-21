# Basic stuff to start bot

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
client.run(token)


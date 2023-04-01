import discord
import os

import asyncio
import random

import requests
import json


import sqlite3
import replit

from replit import db

from discord.ext import commands
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv


from keep_bot_alive import keep_bot_alive
load_dotenv()

""" conn = sqlite3.connect('database.db')
db = conn.cursor() """
#token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
voice_client = None


# Massive of emotional damage
emotional_damage = [
    'bad','sad','rat','worm','bitch'
    ]

# Massive of oposite words
emotional_rise = [
    'Take cockout of your mouth',
    'Well just think like Justin Beieber',
    'Barbara Strayzand',
    'Kurwa match',
    'Pidr'
    ]

def get_quote():
    otvet = requests.get("https://api.adviceslip.com/advice")
    json_data = json.loads(otvet.text)
    if 'slip' in json_data and 'advice' in json_data['slip']:
        citata = json_data['slip']['advice']
        return citata
    else:
        return "Sorry, I couldn't find any advice at the moment."


db = {}


def update_emotional_rise(emotional_rise_message):
    if "rise_message" in db.keys():
        rise_message = db["rise_message"]
        rise_message.append(emotional_rise_message)
        db["rise_message"] = rise_message
    else:
        db["rise_message"] = [emotional_rise_message]
    #return

def delete_emotional_rise_message(index_of_message):
    rise_message = db["rise_message"]
    if len(rise_message) > index_of_message:
        del rise_message[index_of_message]
        db["rise_messgae"] = rise_message

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord! And now Online!!! ')

# Not working !info_help
async def info_help(ctx):
    help_str = "List of available commands '!' + 'command':\n\n"
    help_str += "!proverka --> A test command.\n"
    help_str += "!play_any_sound --> Play a sound in the voice channel.\n"
    help_str += "!info_help --> Display this message.\n"
    await ctx.send(help_str)

# Not working !proverka

@bot.command()
async def proverka(ctx):
    await ctx.reply("Dong Cong Cock Вот тебе урок!")


# Not working sound function !play_any_sound -> using sound file music/scra.wav
@bot.command()
async def play_any_sound(ctx):
    global voice_client
    if voice_client is None:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
    any_sound_file = "music/scra.wav"
    audio_source = discord.FFmpegPCMAudio(executable="ffmpeg", source=any_sound_file)
    voice_client.play(audio_source)
    await ctx.send("Scibadee Paa Poo!")
    while voice_client.is_playing():
        await asyncio.sleep(1)
    await voice_client.disconnect()
    voice_client = None

""" async def on_ready():
    global voice_client
    print("The bot is online!")
    if voice_client is None:
        voice_channel = bot.get_channel(1081256139276169331)
        if voice_channel:
            voice_client = await voice_channel.connect() """

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    msg = message.content


    if msg.lower() in ['/hello', '/hi', '/whatsup', '/privet', '/hey']:
        responses = ['Hello!', 'Hi there!', 'What\'s up?', 'Greetings!', 'Hey!', 'Are you Petushara?']
        response = random.choice(responses)
        await message.channel.send(response)

    if message.content.lower() in['/citata', '/quote', '/smart', '/inspire']:
        citata = get_quote()
        await message.channel.send(citata)
    
    vybor = emotional_rise

    if "rise_message" in db.keys():
        vybor = vybor + db["rise_message"]
    
    if any(slovo in msg for slovo in emotional_damage):
        await message.channel.send(random.choice(vybor))
    
    if msg.startswith("$new"):
        rise_message = msg.split("$new", 1)[1]
        update_emotional_rise(rise_message)
        await message.channel.send("New Encouraging message added.")
    
    if msg.startswith("$del"):
        rise_message = []
        if "rise_message" in db.keys():
            index_rise_message = int(msg.split("$del", 1)[1])
            delete_emotional_rise_message(index_rise_message)
            rise_message = db["rise_message"]
        await message.channel.send(rise_message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("Command not found.")
    


    


#print(os.getenv('TOKEN'))

keep_bot_alive()
bot.run(os.getenv('TOKEN'))


""" @bot.command()
async def play_any_sound(ctx):
    global voice_client
    if voice_client is None:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
    any_sound_file = "music/scra.wav"
    bot_sound = AudioSegment.from_file(any_sound_file)
    play(bot_sound)
    await ctx.send("Scibadee Paa Poo!")

    #await ctx.voice_client.play(any_sound_file)
    await voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=any_sound_file))

    while play.is_playing():
        await asyncio.sleep(1)
    await voice_client.disconnect()
    #await ctx.send("Scibadee Paa Poo!")
    voice_client = None """
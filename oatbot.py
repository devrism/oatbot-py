# pylint: disable=invalid-name
#!/usr/bin/env python3

"""
oatbot created by devrism, exclusively for the friend chat junk land mark II Discord server
"""

import discord
from res.configtest import *
from modules.thonkify.thonkify import thonkify
from modules.weather.weather import getWeather
from modules.activityGroup.activityGroup import *

client = discord.Client()
playingStatus = discord.Game('socially safe games') #name of the game the bot plays
PREFIX = 'oat' #TODO: add function to change prefix later
separator = '/'

#Initialize ActivityManager
activityManager = ActivityGroupManager()

@client.event
async def on_ready():
    """logging stuff, can delete later"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(status=discord.Status.online, activity=playingStatus)

@client.event
async def on_resumed():
    # change game status
    await client.change_presence(status=discord.Status.online, activity=playingStatus)
    
@client.event
async def on_message(message):
    lower_msg = message.content.lower() #we want to be able to use commands regardless of case

    if message.author.bot is False:

        ############################################## slash commands ################################################
        if lower_msg.startswith('/weather '): #weather
            reply = getWeather(message, weatherKey)
            await message.channel.send("This is under construction, sorry!")

        if lower_msg.startswith('/clap '): 
            reply = message.content[5:].replace(" ", " 👏 ") + " 👏"
            await message.channel.send(reply)
            
        #thonkify 
        elif lower_msg.startswith('/thonkify '):
            if len(message.content) > 60:
                await message.channel.send('Error: message cannot be over 60 characters')
            else:
                thonkify(message)
                await message.channel.send(file=discord.File('result.png'))

        ############################################## reactions #####################################################

        #responds to oats with bandaid emoji
        elif '/oat' in lower_msg:
            await message.add_reaction('name:304863358325358602')
            # await client.add_reaction(message, 'name:457245675072258078')
            
        #bacAgreed
        elif 'naruhodo' in lower_msg:
            emoji = client.get_emoji(555426896805101586)
            await message.add_reaction(emoji)

        #Dr. Pimplepopper is gross af
        elif 'pimplepopper' in lower_msg:
            await message.add_reaction('\U0001F922')

        #put that table back where it came from, or so help me
        elif '(╯°□°）╯︵ ┻━┻' in lower_msg:
            await message.channel.send('┬──┬ ノ( ゜-゜ノ);;')

        elif 'yeet' in lower_msg:
            await message.channel.send('yeet!')

        elif 'good morn' in lower_msg: 
            await message.add_reaction('\U0001F31E')

        elif 'good night' in lower_msg or 'goodnight' in lower_msg: 
            await message.add_reaction('\U0001F31A')

        elif 'thank' in lower_msg and 'oatbot' in lower_msg: 
            emoji = client.get_emoji(674420341342470166)
            await message.add_reaction(emoji)
            
        #if the message starts with our designated prefix, process the command
        #if message.content.startswith(PREFIX+separator):
        #    await client.send_message(message.channel, parseCommand(message, separator, PREFIX))

client.run(key)

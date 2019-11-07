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

PREFIX = 'oat' #TODO: add function to change prefix later
separator = '/'
playing = 'with secrets, puhu' #name of the game the bot plays

#Initialize ActivityManager
activityManager = ActivityGroupManager()

@client.event
async def on_ready():
    """logging stuff, can delete later"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name=playing))

@client.event
async def on_resumed():
    # change game status
    await client.change_presence(game=discord.Game(name=playing))

@client.event
async def on_message(message):
    lower_msg = message.content.lower() #we want to be able to use commands regardless of case

    if message.author.bot is False:

        ############################################## slash commands ################################################
        if lower_msg.startswith('/group ') and message.channel.id == '316299333714706433': 
            nick = message.author.nick
            role = message.author.roles
            reply = activityManager.createGroup("testGroup", message.author.id)
            await client.send_message(message.channel, reply)
            reply = activityManager.addMemberToGroup("testGroup", "<@261157845376958464>")
            await client.send_message(message.channel, reply)
            await client.send_message(message.channel, message.author.id)
            reply = activityManager.deleteGroup("testGroup", message.author.id)

        if lower_msg.startswith('/weather '): #weather
            reply = getWeather(message, weatherKey)
            await client.send_message(message.channel, reply)

        #responds to oats with bandaid emoji
        elif '/oat' in lower_msg:
            await client.add_reaction(message, 'name:304863358325358602')
            # await client.add_reaction(message, 'name:457245675072258078')
            
        #thonkify 
        elif '/thonkify ' in lower_msg:
            if len(message.content) > 60:
                await client.send_message(message.channel, 'Error: message cannot be over 60 characters')
            else:
                thonkify(message)
                await client.send_file(message.channel, 'result.png')

        ############################################## reactions #####################################################

        #bacAgreed
        if 'naruhodo' in lower_msg:
            emoji = discord.utils.get(client.get_all_emojis(), id='555426896805101586')
            await client.add_reaction(message, emoji)

        #Dr. Pimplepopper is gross af
        if 'pimplepopper' in lower_msg:
            await client.add_reaction(message, '\U0001F922')

        #put that table back where it came from, or so help me
        elif '(╯°□°）╯︵ ┻━┻' in lower_msg:
            await client.send_message(message.channel, '┬──┬ ノ( ゜-゜ノ);;')

        elif 'yeet' in lower_msg:
            await client.send_message(message.channel, 'yeet!')

        #if the message starts with our designated prefix, process the command
        #if message.content.startswith(PREFIX+separator):
        #    await client.send_message(message.channel, parseCommand(message, separator, PREFIX))

client.run(key)
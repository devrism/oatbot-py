# pylint: disable=invalid-name

"""
oatbot created by devrism, exclusively for the friend chat junk land mark II Discord server
"""

import discord
from config import *
from thonkify import thonkify

client = discord.Client()

PREFIX = 'oat' #TODO: add function to change prefix later
separator = '/'
playing = 'naruhodo' #name of the game the bot plays

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
        #responds to oats with bandaid emoji
        if '/oat' in lower_msg:
            await client.add_reaction(message, 'name:304863358325358602')
            # await client.add_reaction(message, 'name:457245675072258078')

        #bacAgreed
        if 'naruhodo' in lower_msg:
            emojiList = client.get_all_emojis()
            for emoji in emojiList:
                if emoji.id == '555426896805101586':
                    await client.add_reaction(message, emoji)
                    break
            
        #thonkify 
        elif '/thonkify ' in lower_msg:
            if len(message.content) > 60:
                await client.send_message(message.channel, 'Error: message cannot be over 60 characters')
            else:
                thonkify(message)
                await client.send_file(message.channel, 'result.png')

        #Dr. Pimplepopper is gross af
        elif 'pimplepopper' in lower_msg:
            await client.add_reaction(message, '\U0001F922')

        #put that table back where it came from, or so help me
        elif '(╯°□°）╯︵ ┻━┻' in lower_msg:
            await client.send_message(message.channel, '┬──┬ ノ( ゜-゜ノ);;')

        #music channel - add all youtube links to spotify playlist
        elif '/spotifyadd ' in lower_msg: #bots channel 
            youtubeLink = lower_msg[12:]
            await client.send_message(message.channel, youtubeLink)

        elif 'yeet' in lower_msg:
            await client.send_message(message.channel, 'yeet!')

        #if the message starts with our designated prefix, process the command
        #if message.content.startswith(PREFIX+separator):
        #    await client.send_message(message.channel, parseCommand(message, separator, PREFIX))

client.run(key)

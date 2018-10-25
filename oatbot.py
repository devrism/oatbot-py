# pylint: disable=invalid-name

"""
oatbot created by devrism, exclusively for the friend chat junk land mark II Discord server
"""

import discord
from commandparser import parseCommand
from config import *
from thonkify import thonkify
import Cleverbotio

client = discord.Client()

PREFIX = 'oat' #TODO: add function to change prefix later
separator = '/'
playing = 'thonkify | 50% done' #name of the game the bot plays

#cleverbot
chatbot = Cleverbotio.Cleverbot(cleverbotUser, cleverbotKey, nick = 'oatbot')
chatbot.create_session()

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
    """
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    """
    lower_msg = message.content.lower() #we want to be able to use commands regardless of case

    #responds to oats with bandaid emoji
    if '/oat' in lower_msg:
        await client.add_reaction(message, 'name:304863358325358602')

    #thonkify 
    elif '/thonkify' in lower_msg:
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

    elif 'yeet' in lower_msg:
        await client.send_message(message.channel, 'yeet!')

    #cleverbot
    """
    elif oatbotId in lower_msg or oatbotIdNick in lower_msg:
        lower_msg = lower_msg[22:]
        chatbotReply = chatbot.say(lower_msg)
        await client.send_message(message.channel, chatbotReply['response'].strip('\"'))
    """

    #if the message starts with our designated prefix, process the command
    if message.content.startswith(PREFIX+separator):
        await client.send_message(message.channel, parseCommand(message, separator, PREFIX))

async def keepawake():
    channels = client.get_all_channels()
    asyncio.sleep(50)

client.run(key)

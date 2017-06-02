# pylint: disable=invalid-name

"""
oatbot created by devrism, exclusively for the friend chat junk land mark II Discord server
link to invite:
https://discordapp.com/oauth2/authorize?client_id=316389024191479809&scope=bot&permissions=0
"""
#import asyncio
import discord
from commandparser import parseCommand

client = discord.Client()

PREFIX = 'oat' #TODO: add function to change prefix later
separator = '/'
playing = 'with oats' #name of the game the bot plays


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
    """trying to change game status"""
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

    #put that table back where it came from, or so help me
    if '(╯°□°）╯︵ ┻━┻' in lower_msg:
        await client.send_message(message.channel, '┬──┬ ノ( ゜-゜ノ);;')

    #if the message starts with our designated prefix, process the command
    if message.content.startswith(PREFIX+separator):
        await client.send_message(message.channel, parseCommand(message, separator, PREFIX))

client.run('MzE2Mzg5MDI0MTkxNDc5ODA5.DAUong.ZXvbBbeGyjR_QWxFNNFilZqafYM')

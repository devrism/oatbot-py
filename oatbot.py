import discord
import asyncio
#link to invite: https://discordapp.com/oauth2/authorize?client_id=316389024191479809&scope=bot&permissions=0

client = discord.Client()

@client.event
async def on_ready():
    """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    """

@client.event
async def on_message(message):
    lower_msg = message.content.lower() #we want to be able to use commands regardless of case
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

    if lower_msg.startswith('/oat'):
        await client.add_reaction(message, 'name:304863358325358602')

client.run('MzE2Mzg5MDI0MTkxNDc5ODA5.DAUong.ZXvbBbeGyjR_QWxFNNFilZqafYM')

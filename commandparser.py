# pylint: disable=invalid-name

def parseCommand(message, separator, prefix):
    """parses commands for the bot, returns a string as a message"""
    response = "This feature is under development!"
    splitmsg = message.content.split('/')

    if splitmsg[1] == 'help':
        response = 'Help documentation to be added later.'

    return response

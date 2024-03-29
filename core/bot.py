import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from helper.singleton import singleton

load_dotenv()

INITIAL_EXTENSIONS = [
    'cogs.example',
    'cogs.reaction'
]


@singleton
class GDSCBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        if 'command_prefix' not in kwargs:
            kwargs['command_prefix'] = '!'

        if 'intents' not in kwargs:
            intents = discord.Intents.all()
            intents.message_content = True
            intents.members = True
            intents.typing = True
            intents.presences = True
            kwargs['intents'] = intents

        # for extension in INITIAL_EXTENSIONS:
        #     try:
        #         self.load_extension(extension)
        #     except Exception as e:
        #         print(f'Failed to load extension {extension}. error: {e}')

        super().__init__(*args, **kwargs)


    def run(self, *args, **kwargs):
        token = os.getenv('DISCORD_TOKEN')
        super().run(token, *args, **kwargs)

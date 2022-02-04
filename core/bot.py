import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from helper.singleton import singleton

load_dotenv()


@singleton
class DSCBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        if 'command_prefix' not in kwargs:
            kwargs['command_prefix'] = '!'
        if 'intents' not in kwargs:
            kwargs['intents'] = discord.Intents.all()
        super().__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        token = os.getenv('DISCORD_TOKEN')
        super().run(token, *args, **kwargs)

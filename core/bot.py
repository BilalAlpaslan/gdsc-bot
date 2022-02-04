import discord
from discord.ext import commands
from discord_slash import SlashCommand

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot)


def get_slash() -> SlashCommand:
    return slash


def get_bot() -> commands.Bot:
    return bot

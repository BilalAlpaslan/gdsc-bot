
import discord
from core.bot import get_bot

bot = get_bot()


async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name='!help'))

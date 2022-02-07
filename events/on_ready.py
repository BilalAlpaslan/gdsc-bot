
import discord
from core.bot import GDSCBot
from events.on_member_join import start_watch

bot = GDSCBot()


async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name='!help'))

    # for wacth new member with using invite code
    await start_watch()
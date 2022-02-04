import os
from unicodedata import name

from dotenv import load_dotenv

from commands.welcome_channel import welcome_channel
from commands.welcome_message import welcome_message
from commands.open_ticket import open_ticket
from commands.slash import _test
from core.bot import get_bot, get_slash
from events.on_member_join import on_member_join
from events.on_ready import on_ready

load_dotenv()
bot = get_bot()
slash = get_slash()

bot.event(on_ready)
bot.event(on_member_join)


bot.command(
    name='welcomeChannel',
    help='Change the channel for the welcome message'
)(welcome_channel)

bot.command(
    name='welcomeMessage',
    help='Change the welcome message'
)(welcome_message)

bot.command(
    name='openTicket',
    help='Open a ticket'
)(open_ticket)

slash.slash(name='test')(_test)


def main():
    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)

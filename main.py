
from commands.open_ticket import open_ticket
from commands.welcome_channel import welcome_channel
from commands.welcome_message import welcome_message
from core.bot import GDSCBot
from events.on_member_join import on_member_join
from events.on_ready import on_ready

bot = GDSCBot()

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


def main():
    bot.run()


if __name__ == '__main__':
    main()


from core.bot import GDSCBot
from models.guild import get_or_create_guild

bot = GDSCBot()


async def open_ticket(ctx, *args):
    reason = ' '.join(args)
    guild = await get_or_create_guild(ctx.guild.id)
    if not guild.ticketCh:
        await ctx.send('No ticket channel set!')
        return
    await guild.ticketCh.send(f'{ctx.author.mention} opened a ticket. Reason: {reason}')

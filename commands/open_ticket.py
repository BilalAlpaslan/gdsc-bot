
from core.bot import get_bot
from models.guild import get_or_create_guild

bot = get_bot()


async def open_ticket(ctx, *args):
    reason = ' '.join(args)
    guild = await get_or_create_guild(ctx.guild.id)
    if not guild.ticketCh:
        await ctx.send('No ticket channel set!')
        return
    await guild.ticketCh.send(f'{ctx.author.mention} opened a ticket. Reason: {reason}')

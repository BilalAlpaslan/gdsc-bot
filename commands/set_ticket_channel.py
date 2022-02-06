from companents.ticket_button import Counter
from models.guild import get_or_create_guild
import discord


async def set_ticket_channel(ctx: discord.ext.commands.Context):
    guild = await get_or_create_guild(ctx.guild.id)
    channel = ctx.channel
    category = channel.category

    guild.ticket_channel = channel
    guild.ticket_category = category

    view = Counter()

    await ctx.send("Get ticket from here", view=view)

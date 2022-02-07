from companents.ticket_button import Counter
from models.guild import get_or_create_guild
import discord


async def set_ticket_channel(ctx: discord.ext.commands.Context, channel: discord.TextChannel):
    if channel is None:
        channel = ctx.channel

    if channel.category is None:
        await ctx.send("Channel must be in a category")
        return

    guild = await get_or_create_guild(ctx.guild.id)
    guild.ticket_channel = channel
    guild.ticket_category = channel.category

    view = Counter()

    await ctx.send("Get ticket from here", view=view)

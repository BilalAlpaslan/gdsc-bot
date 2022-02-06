from companents.ticket_button import Counter
from models.guild import get_or_create_guild
import discord


async def set_moderate_tag(ctx: discord.ext.commands.Context, tag: str):
    guild = await get_or_create_guild(ctx.guild.id)
    guild.moderate_tag = tag
    await ctx.send("Moderate tag set to {}".format(tag))

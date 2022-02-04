import discord
from discord_slash import SlashContext

async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])
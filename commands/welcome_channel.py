from models.guild import get_or_create_guild
import discord


async def welcome_channel(ctx, channel: discord.TextChannel):
    guild = await get_or_create_guild(ctx.guild.id)
    guild.welcomeCh = channel
    await ctx.send(f'Welcome channel set to {channel.mention}')

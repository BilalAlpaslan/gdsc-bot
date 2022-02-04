from pydantic import BaseModel
import discord

from core.bot import DSCBot

bot = DSCBot()

class Guild(BaseModel):
    guild: discord.Guild
    welcomeCh: discord.TextChannel
    ticketCh: discord.TextChannel
    welcomeMessage: str = 'Welcome {member.mention} to {member.guild.name}!'

    class Config:
        arbitrary_types_allowed = True


guilds = {}


async def get_or_create_guild(guild_id):
    if guild_id in guilds:
        return guilds[guild_id]
    guild = bot.get_guild(guild_id)
    guilds[guild_id] = Guild(guild=guild, welcomeCh=guild.system_channel, ticketCh=guild.system_channel)
    return guilds[guild_id]

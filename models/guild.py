from pydantic import BaseModel
import discord

from core.bot import GDSCBot

bot = GDSCBot()

class Guild(BaseModel):
    guild: discord.Guild
    welcomeCh: discord.TextChannel
    ticket_channel: discord.TextChannel = None
    ticket_category: discord.CategoryChannel = None
    moderate_tag: str = None
    welcomeMessage: str = 'Welcome {member.mention} to {member.guild.name}!'

    class Config:
        arbitrary_types_allowed = True


guilds = {}


async def open_ticket(guild: Guild, user: discord.Member):
    if guild.ticket_channel is None:
        return
    #  create a new channel with the name of the user in the guild category
    new_channel = await guild.guild.create_text_channel(
        name=user.name,
        category=guild.ticket_category,
        reason='Creating ticket channel'
    )
    await new_channel.set_permissions(user, read_messages=True, send_messages=True)
    await new_channel.set_permissions(bot.user, read_messages=True, send_messages=True)
    #  send the welcome message
    await new_channel.send(guild.welcomeMessage.format(member=user))
    if guild.moderate_tag is not None:
        await new_channel.send(f"please wait few minutes for the {guild.moderate_tag} to review your ticket")



async def get_or_create_guild(guild_id):
    if guild_id in guilds:
        return guilds[guild_id]
    guild = bot.get_guild(guild_id)
    guilds[guild_id] = Guild(guild=guild, welcomeCh=guild.system_channel, ticketCh=guild.system_channel)
    return guilds[guild_id]

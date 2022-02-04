
import discord
from models.gif import get_random_gif
from models.guild import get_or_create_guild
from models.user import users


async def on_member_join(member: discord.Member):
    print(f'{member} has joined the server!')
    guild = await get_or_create_guild(member.guild.id)
    gif = await get_random_gif("hello")
    await guild.welcomeCh.send(guild.welcomeMessage.format(member=member, gif=gif))
    await guild.welcomeCh.send(gif.url)

    if member.id in users:
        user = users.get(member.id)
        role = member.guild.get_role(user.tags_with_id[0])
        await member.add_roles(role)

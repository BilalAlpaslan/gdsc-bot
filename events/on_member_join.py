
import discord
from core.bot import GDSCBot
from models.gif import get_random_gif
from models.guild import get_or_create_guild
from models.user import users

invites = {}
bot = GDSCBot()


async def start_watch():
    for guild in bot.guilds:
        invites[guild.id] = await guild.invites()


def find_invite_by_code(invite_list, code):
    for inv in invite_list:
        if inv.code == code:
            return inv


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

    invites_before_join = invites[member.guild.id]
    invites_after_join = await member.guild.invites()

    for invite in invites_before_join:
        if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:

            print(f"Member {member.name} Joined")
            print(f"Invite Code: {invite.code}")
            print(f"Inviter: {invite.inviter}")

            invites[member.guild.id] = invites_after_join
            
            if invite.code == "AAGYg2gC5Z":
                await member.add_roles(member.guild.get_role(938504866484080680))

            return


# import discord

# from discord.ext import commands


# class Roles:

#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command(name='addrole', help='Add a role to a user')
#     async def addrole(self, ctx, role: discord.Role, user: discord.Member):
#         await user.add_roles(role)
#         await ctx.send(f'{user.mention} has been given the {role.name} role.')


# def setup(bot: commands.Bot):
#     bot.add_cog(Roles(bot))

from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client  # sets the client variable so we can use it in cogs

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example Cog is ready!')

    @commands.command()
    async def command(self, ctx):
        print('Example command ran!')


def setup(client):
    client.add_cog(Example(client))

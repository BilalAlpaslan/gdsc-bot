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

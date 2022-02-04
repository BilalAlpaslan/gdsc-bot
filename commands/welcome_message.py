
from models.guild import get_or_create_guild


async def welcome_message(ctx, *, message: str):
    guild = await get_or_create_guild(ctx.guild.id)
    guild.welcomeMessage = message
    await ctx.send(f'Welcome message set to: \n {message}')

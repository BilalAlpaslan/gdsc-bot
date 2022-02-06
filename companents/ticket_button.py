from itertools import count
import discord
from models.guild import get_or_create_guild, open_ticket


class Counter(discord.ui.View):
    def __init__(self):
        self.count = 0
        super().__init__()

    @discord.ui.button(label='Get Ticket', style=discord.ButtonStyle.red)
    async def get_ticket(self, button: discord.ui.Button, interaction: discord.Interaction):
        colors = [
            discord.ButtonStyle.green,
            discord.ButtonStyle.red,
        ]
        button.style = colors[self.count % len(colors)]
        self.count += 1
        await interaction.message.edit(view=self)
        
        user: discord.Member = interaction.user
        guild: discord.Guild = await get_or_create_guild(user.guild.id)
        await open_ticket(guild, user)

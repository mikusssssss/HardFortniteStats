from redbot.core import commands
import discord

class SayHello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="say", description="repeats the message you sent")
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(f"{interaction.user.display_name}: {message}")

from discord.ext import commands
from discord.commands import slash_command

class Greet(commands.cog):
    def __init__(self, bot):
        self.bot = bot
        
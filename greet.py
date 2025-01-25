import discord
from discord.ext import commands
from discord.commands import slash_command

class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command()
    async def greet(self, ctx):
        await ctx.respond(f"Na du nudel {ctx.author.menton}")
        
        
        
def setup(bot):
    bot.add_cog(Greet(bot))
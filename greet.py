import discord
from discord.ext import commands

class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def greet(self, ctx):
        await ctx.respond(f"Na du nudel {ctx.author.mention}")


def setup(bot):
    bot.add_cog(Greet(bot))

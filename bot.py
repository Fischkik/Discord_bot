import discord
from discord.commands import Option

intents = discord.Intents.default()
bot = discord.Bot(
    intents=intents,
    debug_guilds=[1332722155342790759]
    )


@bot.event
async def on_ready():
    print("bot is working")

bot.run("")

@bot.slash_command(descrption="Moin")
async def greet(ctx, user: Option(discord.Member, "greetable user")):
    await ctx.respond(f"Moin {user.mention}")
    
bot.run("")
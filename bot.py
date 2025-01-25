import discord

bot = discord.bot(debug_guilds=[1332722155342790759])


@bot.event
async def on_ready():
    print("bot is working")

bot.run("")
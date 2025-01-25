import discord
from discord.commands import Option

def get_dc_api() -> str:
    with open("api.txt","r") as api_key:
        return api_key.readlines()[0]
        

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(
    intents=intents,
    debug_guilds=[1332722155342790759]
    )


@bot.event
async def on_ready():
    print("bot is working")

bot.load_extension("twitch_background")
bot.load_extension("greet")  
bot.run(get_dc_api())
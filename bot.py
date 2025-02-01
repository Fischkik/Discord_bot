import discord
import discord.ext.commands
import asyncio
from twitch_backround import Twitchbackground
from greet import Greet


def get_dc_api() -> str:
    with open("api.txt", "r") as api_key:
        return api_key.readlines()[0]


intents = discord.Intents.default()
intents.members = True

bot = discord.ext.commands.Bot(
    command_prefix="", intents=intents, debug_guilds=[1332722155342790759]
)


@bot.event
async def on_ready():
    print("bot is working")


async def main():
    await bot.add_cog(Twitchbackground(bot))
    await bot.add_cog(Greet(bot))
    await bot.start(get_dc_api())
    
if __name__ == "__main__":
    asyncio.run(main())

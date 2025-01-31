from twitchAPI.twitch import Twitch
from discord.ext import commands, tasks


class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_twitch_api(self) -> list:
        with open("api.txt", "r") as api_key:
            return api_key.readlines()[1:]

    async def live_huebi(self):
        channel = await self.bot.fetch_cahnnel(1332758805146107964)
        user = await self.bot.fetch_user(690557122194309130)
        await channel.send(
            f"hey {user.mention} huebi ist live schnell \n"
            "https://www.twitch.tv/huebi"
        )

    @tasks.loop(seconds=1)
    async def twitch_noti(self):
        client_id = self.get_twitch_api()[2]
        client_secret = self.get_twitch_api[1]
        twitch = await Twitch(client_id, client_secret)
        await twitch.authenticate_app()
        user_info = await twitch.get_users(logins=["huebi"])
        if user_info["data"]:
            print("jooo der ist live")
            user_id = user_info["data"][0]["id"]
            streams = await twitch.get_streams(user_id=[user_id])
            if streams["data"]:
                await self.live_huebi()

def setup(bot):
    bot.add_cog(Task(bot))

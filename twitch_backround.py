from twitchAPI.twitch import Twitch
from discord.ext import commands, tasks
import datetime

class Twitchbackground(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.used = True

    def check_tomorrow(self):
        today = datetime.datetime.now()
        tomorrow = today + datetime.timedelta(days=1)
        if today.date() == tomorrow.date():
            self.used = True
        
    
    def get_twitch_api(self) -> list:
        with open("api.txt", "r") as api_key:
            return api_key.readlines()

    @commands.Cog.listener()
    async def on_ready(self):
        self.twitch_noti.start()

    async def live_huebi(self):
        channel = await self.bot.fetch_channel(1332758805146107964)
        user = await self.bot.fetch_user(690557122194309130)
        await channel.send(
            f"hey {user.mention} huebi ist live schnell \n"
            "https://www.twitch.tv/huebi"
        )

    @tasks.loop(seconds=6)
    async def twitch_noti(self):
        if self.bot.is_closed():
            return
        print("checking for huebi")
        self.check_tomorrow()
        client_id = self.get_twitch_api()[2].strip()
        client_secret = self.get_twitch_api()[1].strip()
        twitch = await Twitch(client_id, client_secret)
        # Use async for to handle the async generator
        async for user_info in twitch.get_users(logins=["huebi"]):
            if user_info:
                user_id = user_info.id

                # Use async for to handle the async generator
                async for streams in twitch.get_streams(user_id=[user_id]):
                    if streams and self.used:
                        await self.live_huebi()
                        self.used = False


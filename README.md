
# My first Discord bot project

### What you need

* Both libaries(Twitch and Discord)
* All the api keys written to there line

### How to Use

You run the bot.py script and change the channel ids and user ids to yours.
```python
channel = await self.bot.fetch_channel(1332758805146107964)
user = await self.bot.fetch_user(690557122194309130)
```

You might also change the streamers name in my case it was **huebi**.
```python
async for user_info in twitch.get_users(logins=["huebi"]):
```

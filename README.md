
# My first Discord bot project

At the Moment the only usecase is to get notified when a streamer goes live on Twitch.

### What you need

* Both libaries Twitch and Discord(pip).
* All the api keys written to there line in the api.txt file.
  - ```
    1 //your Discord bot token
    2 //your Twitch app secret
    3 // your Twitch  app id
    ```

### How to Use

Run the bot.py script.
>[!IMPORTANT]
>Change the channel ids and user ids to yours.
```python
channel = await self.bot.fetch_channel(1332758805146107964)
user = await self.bot.fetch_user(690557122194309130)
```

You might also change the streamers name in my case it was [Huebi](https://www.twitch.tv/huebi).
```python
async for user_info in twitch.get_users(logins=["huebi"]):
```


### New Features of the bot will follow if I have got some new Ideas.

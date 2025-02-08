import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.help_message = """
```
!help - displays all available commands
!p <song name> - finds the song on youtube and plays it in the current channel
!q - will display the current queue of songs
!skip - skips the current song being played
!clear - stops the music being played and clears the queue
!leave - disconnects the bot from the voice channel
!pause - pauses the current song being played OR resumes if already paused
!resume - resumes the current song that was playing
```
"""
        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

        await self.send_to_all(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.semd(msg)

    @commands.command(name="help", help="Displays all the supported commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
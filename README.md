# code to use for already downloaded audios on my pc

# @client.command(pass_context = True)
# async def pause(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send("Nothing is currently playing, nothing to pause")

# @client.command(pass_context = True)
# async def resume(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_pause():
#         voice.resume()
#     else:
#         await ctx.send("No song is paused at the moment, cannot resume anything")

# @client.command(pass_context = True)
# async def play(ctx):
#     voice = ctx.guild.voice_client

# @client.command(pass_context = True)
# async def stop(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     voice.stop()

# #commands for joining
# @client.command(pass_context = True)
# async def join(ctx):
#     if (ctx.author.voice):
#         channel = ctx.message.author.voice.channel
#         await channel.connect()
#     else:
#         await ctx.send("")

# #commands for leaving
# @client.command(pass_context = True)
# async def leave(ctx):
#     if(ctx.voice_client):
#         await ctx.guild.voice_client.disconnect()
#         await ctx.send("Walter has left the voice channel")
#     else:
#         await ctx.send("I am not currently in a voice channel")
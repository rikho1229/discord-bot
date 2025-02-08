import discord
from discord.ext import commands
import requests
import json
import os, asyncio
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions

from apikey import BOTTOKEN #imports the key from the apikey file
from help_cog import help_cog
from music_cog import music_cog #importing from music_cog file

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

#disabling the default help command
client.remove_command('help')
#adding cogs
client.add_cog(help_cog(client))
client.add_cog(music_cog(client))

@client.event #to signify that the bot is ready to recieve commands
async def on_ready():
    print("Bot is ready for use!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = "!help"))
    await client.add_cog(help_cog(client))
    await client.add_cog(music_cog(client))
    print("-------------------------")

@client.event
async def on_member_join(member):
    channel = client.get_channel(811802033673207820)
    welcome_message = f"{member.mention} has joined the server!"
    await channel.send(welcome_message)

#detecting a message and giving and automatic response to that message
@client.event
async def on_message(message):
    if message.content == "bye":
        await message.channel.send("Goodbye, you will not be missed")
    await client.process_commands(message) #this line of code works to continue the process of other lines being written 

@client.command() #this is what the user is going to type in the chat for the bot to respond to
async def hello(ctx):
    await ctx.send("Hello, I am Walter.")

@client.command(name="cs")
async def computer_science(ctx):
    embed = discord.Embed(
        title='Computer Science Degree Calendar',
        description='Click the link below to view the Computer Science degree calendar:',
        color=discord.Color.blue()
    )
    embed.add_field(name='Degree Calendar Link', value='[Computer Science Calendar](https://calendar.uoguelph.ca/undergraduate-calendar/programs-majors-minors/computer-science-cs/#requirementstext)', inline=False)
    embed.set_footer(text='Univeristy Of Guelph')

    await ctx.send(embed=embed)

@client.command(name="seng")
async def software_engineering(ctx):
    embed = discord.Embed(
        title='Software Engineering Degree Calendar',
        description='Click the link below to view the Software Engineeringe degree calendar:',
        color=discord.Color.blue()
    )
    embed.add_field(name='Degree Calendar Link', value='[Software Engineering Calendar](https://calendar.uoguelph.ca/undergraduate-calendar/programs-majors-minors/software-engineering-seng/#requirementstext)', inline=False)
    embed.set_footer(text='Univeristy Of Guelph')

    await ctx.send(embed=embed)

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"User {member} has been kicked.")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick members.")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"User {member} has been banned.")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to ban other members.")


client.run(BOTTOKEN)

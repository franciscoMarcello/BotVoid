import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix="-",
                      case_insensitive=True, intents=intents)

client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('OTEyMzM3Mjc3NDU0MjU4MjA2.YZueTQ.qU3RlMeWicQlHkqFT1I6aZUjgYE')